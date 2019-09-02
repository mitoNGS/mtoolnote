#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mtoolnote.classes import Annotator, Field, Variant, Parser
from mtoolnote.models import Main


class HumanVariant(Variant):
    """Class to process a single human variant.

    This class receives a single variant and retrieves the related
    annotations, using the HmtVar db.

    Attributes:
        reference: reference allele
        position: nucleotide position
        alternate: alternate allele
        session: db connection session

    Methods:
        response()
    """

    def __init__(self, reference, position, alternate, session):
        super().__init__(reference, position, alternate)
        self.session = session

    def response(self):
        """Retrieve the related information for the given variant.

        Results are converted to a dictionary by the .to_dict() method of
        each model class. If no results are retrieved, the empty dict is
        returned.
        """
        if self._is_deletion():
            resp = (self.session.query(Main)
                    .filter(Main.ref_rCRS == self.reference,
                            Main.nt_start == int(self.position) + 1,
                            Main.alt == "d")
                    .first())
        elif self._is_insertion():
            resp = (self.session.query(Main)
                    .filter(Main.ref_rCRS == self.reference,
                            Main.nt_start == self.position,
                            Main.alt == ".{}".format(
                                self.alternate.value[len(self.reference):]
                            ))
                    .first())
        else:
            resp = (self.session.query(Main)
                    .filter(Main.ref_rCRS == self.reference,
                            Main.nt_start == self.position,
                            Main.alt == self.alternate.value)
                    .first())

        if resp is None:  # no results found
            return dict()
        return resp.to_dict()


class HumanParser(Parser):
    """Class for a human variant parser.

    This class creates a single variant for each alternate allele found
    in a given vcf record, and associates it with the annotations
    determined by the input headers.

    Attributes:
        record: input vcf record
        headers: input vcf headers to which new annotations are added
        session: db connection session

    Methods:
        parse()
    """

    def __init__(self, record, headers, session):
        super().__init__(record, headers)
        self.session = session

    def parse(self):
        """Parse response from HumanVariant and store them in the headers.

        If no results are retrieved a single . is returned.
        """
        variants = [HumanVariant(self.record.REF, self.record.POS, alt, self.session)
                    for alt in self.record.ALT]
        for variant in variants:
            response = variant.response()
            for field in self.headers:
                field.values = response.get(field.slug, ".")


class HumanAnnotator(Annotator):
    """Class for a human annotator.

    A single db connection is created, and each record in the vcf is
    annotated using it.

    Attributes:
        input_vcf: input vcf file
        output_vcf: output vcf file

    Methods:
        _update_header()
        _is_variation()
        annotate()
        to_csv()
    """

    _HEADERS = (("Locus", "locus", "Locus to which the variant belongs"),
                ("CodonPosition", "codon_position",
                 "Codon position of the variant"),
                ("AaChange", "aa_change", "Aminoacidic change determined"),
                ("Pathogenicity", "pathogenicity",
                 "Pathogenicity predicted by HmtVar"))
    engine = create_engine("sqlite:///data/hmtvar.db")
    Session = sessionmaker(bind=engine)

    def __init__(self, input_vcf, output_vcf):
        super().__init__(input_vcf, output_vcf, self._HEADERS)
        self.session = self.Session()

    def annotate(self):
        """Annotate variants found in the input vcf."""
        # session = self.Session()
        for record in self._reader:
            self._n_alleles.append(len(record.ALT))
            fields = [Field(head[0], head[1], head[2]) for head in self.headers]
            if self._is_variation(record):
                annots = HumanParser(record, fields, self.session)
                annots.parse()
                for field in fields:
                    record.INFO[field.element] = field.values
            self._writer.write_record(record)
        self._reader.close()
        self._writer.close()

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from pkg_resources import resource_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mtoolnote.classes import Annotator, Field, Variant, Parser
from mtoolnote.constants import (
    HEADERS_MAIN, HEADERS_CROSSREF, HEADER_PREDICT, HEADERS_VARIAB,
    HEADERS_HAPLOS
)
from mtoolnote.models import (
    Main, CrossRef, Predict, Variab,
    Haplo_A, Haplo_B, Haplo_D, Haplo_G, Haplo_JT, Haplo_L0, Haplo_L1,
    Haplo_L2, Haplo_L3_star, Haplo_L4, Haplo_L5, Haplo_L6, Haplo_M7, Haplo_M8,
    Haplo_M9, Haplo_M_star, Haplo_N1, Haplo_N2, Haplo_N9, Haplo_N_star,
    Haplo_R0, Haplo_R9, Haplo_R_star, Haplo_U, Haplo_X
)


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
    _HAPLOS = (Haplo_A, Haplo_B, Haplo_D, Haplo_G, Haplo_JT, Haplo_L0,
               Haplo_L1, Haplo_L2, Haplo_L3_star, Haplo_L4, Haplo_L5, Haplo_L6,
               Haplo_M7, Haplo_M8, Haplo_M9, Haplo_M_star, Haplo_N1, Haplo_N2,
               Haplo_N9, Haplo_N_star, Haplo_R0, Haplo_R9, Haplo_R_star,
               Haplo_U, Haplo_X)

    def __init__(self, reference, position, alternate, session):
        super().__init__(reference, position, alternate)
        self.session = session

    def _query_frequency(self):
        """Retrieve data from the haplogroup-specific frequency tables."""
        haplo_dict = {}
        if self._is_deletion():
            for haplo in self._HAPLOS:
                query = (self.session.query(haplo)
                         .filter(haplo.position.startswith(f"{self.position}.0"))
                         .first())
                freq = query.to_dict().get("freq_gap", ".")
                haplo_dict[f"{haplo.__tablename__}"] = freq
        elif self._is_deletion():
            for haplo in self._HAPLOS:
                query = (self.session.query(haplo)
                         .filter(haplo.position.startswith(
                             f"{self.position}.{len(self.alternate.value[0])}"))
                         .first())
                freq = query.to_dict().get("freq_oth", ".")  # TODO: correct?
                haplo_dict[f"{haplo.__tablename__}"] = freq
        else:
            for haplo in self._HAPLOS:
                query = (self.session.query(haplo)
                         .filter(haplo.position.startswith(f"{self.position}.0"))
                         .first())
                try:
                    freq = query.to_dict()[f"freq_{self.alternate.value[0]}"]
                except KeyError:
                    freq = query.to_dict()["freq_oth"]
                haplo_dict[f"{haplo.__tablename__}"] = freq

        return haplo_dict

    def _deletion_query(self):
        """Retrieve data from the Main table when the variant is a deletion."""
        query = (self.session.query(Main)
                 .filter(Main.ref_rCRS == self.reference,
                 Main.nt_start == int(self.position) + 1,
                 Main.alt == "d").first())
        return query

    def _insertion_query(self):
        """Retrieve data from the Main table when the variant is an insertion."""
        query = (self.session.query(Main)
                 .filter(Main.ref_rCRS == self.reference,
                         Main.nt_start == self.position,
                         Main.alt == f".{self.alternate.value[len(self.reference):]}")
                 .first())
        return query

    def _snp_query(self):
        """Retrieve data from the Main table when the variant is a simple SNP."""
        query = (self.session.query(Main)
                 .filter(Main.ref_rCRS == self.reference,
                         Main.nt_start == self.position,
                         Main.alt == self.alternate.value).first())
        return query

    def response(self, predict=False):
        """Retrieve the related information for the given variant.

        Results are converted to a dictionary by the .to_dict() method of
        each model class. If no results are retrieved, the empty dict is
        returned.
        """
        if self._is_deletion():
            query_main = self._deletion_query()
        elif self._is_insertion():
            query_main = self._insertion_query()
        else:
            query_main = self._snp_query()

        if query_main is None:
            return dict()

        idx = query_main.id
        query_crossref = (self.session.query(CrossRef)
                          .filter(CrossRef.id == idx).first())
        query_predict = (self.session.query(Predict)
                         .filter(Predict.id == idx).first())
        query_variab = (self.session.query(Variab)
                        .filter(Variab.id == idx).first())
        query_haplos = self._query_frequency()

        return {**query_main.to_dict(),
                **query_crossref.to_dict(),
                **query_predict.to_dict(),
                **query_variab.to_dict(),
                **query_haplos}


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
        variants = [HumanVariant(self.record.REF, self.record.POS, alt,
                                 self.session)
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
    _HEADERS = (*HEADERS_MAIN, *HEADER_PREDICT, *HEADERS_VARIAB,
                *HEADERS_CROSSREF, *HEADERS_HAPLOS)
    _dbfile = resource_filename(__name__, "data/hmtvar.db")
    engine = create_engine(f"sqlite:///{_dbfile}")
    Session = sessionmaker(bind=engine)

    def __init__(self, input_vcf, output_vcf):
        super().__init__(input_vcf, output_vcf, self._HEADERS)
        self.session = self.Session()

    def annotate(self):
        """Annotate variants found in the input vcf."""
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

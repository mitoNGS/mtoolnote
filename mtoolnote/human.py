#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from pkg_resources import resource_filename
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mtoolnote.classes import Annotator, Field, Variant, Parser
from mtoolnote.constants import HUMAN_HEADERS
from mtoolnote.models import (
    Main, CrossRef, Predict, Variab, Loci, Func_Loci,
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

    def __init__(self, reference, position, alternate, session,
                 crossref=True, predict=True, variab=True, haplos=True):
        super().__init__(reference, position, alternate)
        self.session = session
        self.crossref = crossref
        self.predict = predict
        self.variab = variab
        self.haplos = haplos

    @property
    def _locus(self) -> str:
        """Return the locus to which the variant belongs."""
        query = (self.session.query(Loci)
                 .filter(Loci.nt_start <= self.position,
                         Loci.nt_end >= self.position)
                 .first())
        try:
            locus_name = query.to_dict().get("locus", ".")
            locus_desc = query.to_dict().get("description", ".")
            locus = f"{locus_name} ({locus_desc})"
        except AttributeError:
            locus = "."

        return locus

    @property
    def _func_locus(self):
        """Return the functional locus to which the variant belongs."""
        query = (self.session.query(Func_Loci)
                 .filter(Func_Loci.nt_start <= self.position,
                         Func_Loci.nt_end >= self.position)
                 .first())
        try:
            locus_name = query.to_dict().get("locus", ".")
            locus_desc = query.to_dict().get("description", ".")
            locus = f"{locus_name} ({locus_desc})"
        except AttributeError:
            locus = "."

        return locus

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
            return {
                "nt_start": self.position,
                "ref_rCRS": self.reference,
                "alt": self.alternate,
                "nt_end": self.position,
                "locus": self._locus,
                "func_locus": self._func_locus
            }

        idx = query_main.id
        crossrefs = {}
        predicts = {}
        variabs = {}
        haplos = {}

        if self.crossref:
            query_crossref = (self.session.query(CrossRef)
                              .filter(CrossRef.id == idx).first())
            crossrefs = query_crossref.to_dict()
        if self.predict:
            query_predict = (self.session.query(Predict)
                             .filter(Predict.id == idx).first())
            predicts = query_predict.to_dict()
        if self.variab:
            query_variab = (self.session.query(Variab)
                            .filter(Variab.id == idx).first())
            variabs = query_variab.to_dict()
        if self.haplos:
            haplos = self._query_frequency()

        mains = query_main.to_dict()

        # TODO: Adding func_locus here, but it really should be part of the
        #   Main model
        mains["func_locus"] = self._func_locus

        return {**mains,
                **crossrefs,
                **predicts,
                **variabs,
                **haplos}

    def __repr__(self):
        return ("{}(reference={!r}, position={!r}, alternate={!r}, "
                "session={!r})").format(
            self.__class__.__name__, self.reference, self.position,
            self.alternate, self.session
        )


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

    def __init__(self, record, headers, session,
                 crossref=True, predict=True, variab=True, haplos=True):
        super().__init__(record, headers)
        self.session = session
        self.crossref = crossref
        self.predict = predict
        self.variab = variab
        self.haplos = haplos

    def parse(self):
        """Parse response from HumanVariant and store them in the headers.

        If no results are retrieved a single . is returned.
        """
        variants = [HumanVariant(self.record.REF, self.record.POS, alt,
                                 self.session, crossref=self.crossref,
                                 predict=self.predict, variab=self.variab,
                                 haplos=self.haplos)
                    for alt in self.record.ALT]
        for variant in variants:
            response = variant.response()
            for field in self.headers:
                field.values = response.get(field.slug, ".")

    def __repr__(self):
        return "{}(record={!r}, headers={!r}, session={!r})".format(
            self.__class__.__name__, self.record, self.headers, self.session
        )


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
    _HEADERS = HUMAN_HEADERS
    _dbfile = resource_filename(__name__, "data/mtoolnote.db")
    engine = create_engine(f"sqlite:///{_dbfile}")
    Session = sessionmaker(bind=engine)

    def __init__(self, input_vcf, output_vcf,
                 crossref=True, predict=True, variab=True, haplos=True):
        super().__init__(input_vcf, output_vcf, self._HEADERS)
        self.session = self.Session()
        self.crossref = crossref
        self.predict = predict
        self.variab = variab
        self.haplos = haplos

    def annotate(self):
        """Annotate variants found in the input vcf."""
        for record in self._reader:
            self._n_alleles.append(len(record.ALT))
            fields = [Field(head[0], head[1], head[2]) for head in self.headers]
            if self._is_variation(record):
                annots = HumanParser(record, fields, self.session,
                                     crossref=self.crossref,
                                     predict=self.predict, variab=self.variab,
                                     haplos=self.haplos)
                annots.parse()
                for field in fields:
                    record.INFO[field.element] = field.values
            self._writer.write_record(record)
        self._reader.close()
        self._writer.close()

    def __repr__(self):
        return "{}(input_vcf={!r}, output_vcf={!r})".format(
            self.__class__.__name__, self.input_vcf, self.output_vcf
        )

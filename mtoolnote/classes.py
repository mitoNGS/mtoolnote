#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
# import vcfpy2 as vcfpy
import os
import vcfpy
import allel
from collections import defaultdict
from abc import ABC, abstractmethod

_SPECIES = ("oaries", "ptroglodytes", "scerevisiae", "ecaballus", "fcatus",
            "cfamiliaris", "pabelii", "ggallus", "mmulatta", "rnorvegicus",
            "btaurus", "oanatinus", "sscrofa", "nleucogenys", "chircus",
            "mmusculus", "tguttata", "tnigroviridis", "mgallopavo",
            "mdomestica", "drerio")


class Field:
    """Class to represent a header field.

    This class is used to represent INFO headers and to store annotations
    for each alternate allele found in each variant.

    Attributes:
        element: name of the header element
        slug: name used either on the HmtVar db or in BioMart to refer
            to a specific element of information
        description: long string describing the header
        _values: list of annotation values

    Methods:
        _replace_null()
    """

    def __init__(self, element: str, slug: str, description: str):
        self.element = element
        self.slug = slug
        self.description = description
        self._values = []

    @staticmethod
    def _replace_null(value):
        """Replace null values returned by HmtVar's API (None) with a '.'
        character.

        Args:
            value: value returned by the parser

        Returns:
            '.' if element is None, otherwise the element itself
        """
        if value is None:
            return "."
        return value

    @property
    def values(self):
        """List of values parsed from HmtVar's API for each alternate allele
        of the given variant."""
        return self._values

    @values.setter
    def values(self, value):
        """Update the list of values with a new value.

        Args:
            value: new value to be appended to the list of values
        """
        self._values.append(self._replace_null(value))


class Variant(ABC):
    """Abstract class to process a single variant.

    This class receives a single variant and retrieves the related
    annotations, using the HmtVar db if it is a human variant, or
    retrieving data from BioMart if non-human.

    Attributes:
        reference: reference allele
        position: nucleotide position
        alternate: alternate allele

    Methods:
        _is_deletion()
        _is_insertion()
        response()
    """

    def __init__(self, reference, position, alternate):
        self.reference = reference
        self.position = position
        self.alternate = alternate

    def _is_deletion(self) -> bool:
        """Check whether the current variant refers to a deletion."""
        # e.g. ref CTG | alt C
        return self.alternate.type == "DEL"

    def _is_insertion(self) -> bool:
        """Check whether the current variant refers to an insertion."""
        # e.g. ref C | alt CTG
        return self.alternate.type == "INS"

    @abstractmethod
    def response(self):
        """Retrieve the related information for deletions, insertions and SNPs."""
        pass


class Parser(ABC):
    """Abstract class for a variant parser.

    This class creates a single variant for each alternate allele found
    in a given vcf record, and associates it with the annotations
    determined by the input headers.

    Attributes:
        record: input vcf record
        headers: input vcf headers (with new annotations)

    Methods:
        parse()
    """

    def __init__(self, record, headers):
        self.record = record
        self.headers = headers

    @abstractmethod
    def parse(self):
        """Parse results and store them in the headers."""
        pass


class Annotator(ABC):
    """Abstract class for an annotator.

    This class will be overridden by a HumanAnnotator or NonHumanAnnotator,
    based on the provided organism.

    Attributes:
        input_vcf: input vcf file
        output_vcf: output vcf file

    Methods:
        _update_header()
        _is_variation()
        annotate()
        to_csv()
    """

    def __init__(self, input_vcf, output_vcf, headers):
        self.input_vcf = input_vcf
        self.output_vcf = output_vcf
        self.headers = headers
        self._reader = vcfpy.Reader.from_path(self.input_vcf)
        self._update_header()
        self._writer = vcfpy.Writer.from_path(self.output_vcf,
                                              header=self._reader.header)
        self._n_alleles = []

    def _update_header(self):
        """Update vcf header according to the new annotations."""
        fields = [Field(head[0], head[1], head[2]) for head in self.headers]
        for field in fields:
            self._reader.header.add_info_line(
                vcfpy.OrderedDict([("ID", field.element),
                                   ("Number", "A"),
                                   ("Type", "String"),
                                   ("Description", field.description)])
            )

    @staticmethod
    def _is_variation(record):
        """Check whether at least one of the alternate alleles refer to
        a proper variant."""
        return len(record.ALT) > 0 and all([rec.value != "."
                                            for rec in record.ALT])

    @abstractmethod
    def annotate(self):
        """Annotate variants found in the input vcf."""
        pass

    def to_csv(self):
        """Convert the annotated VCF file to CSV format."""
        base_path, base_name = os.path.split(self.output_vcf)
        csv_name = os.path.splitext(base_name)[0]
        output_csv = os.path.join(base_path, "{}.csv".format(csv_name))

        df = allel.vcf_to_dataframe(self.output_vcf, fields="*",
                                    alt_number=max(self._n_alleles))

        df.fillna(".", inplace=True)
        to_merge = [col for col in df.columns
                    if "_" in col and col.split("_")[-1].isdigit()]
        # dictionary of new columns names -> columns to merge
        col_dict = defaultdict(list)
        for col in to_merge:
            new_col = "_".join(col.split("_")[:-1])
            col_dict[new_col].append(col)
        # merge columns and drop duplicate columns
        for new_col, old_cols in col_dict.items():
            # get index of the first column of the set to be merged
            col_idx = df.columns.get_loc(old_cols[0])
            merged_col = df[old_cols].astype(str).apply(lambda x: ";".join(x),
                                                        axis=1)
            df.drop(old_cols, axis=1, inplace=True)
            df.insert(loc=col_idx, column=new_col, value=merged_col.values)

        df.to_csv(output_csv, index=False)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import apybiomart as apy
from concurrent.futures import ThreadPoolExecutor
from mtoolnote.classes import Field, Variant, Parser, Annotator, _SPECIES


# TODO: these two can be deleted, only keeping them here for reference
_ATTRIBUTES = (
    "allele", "chr_name", "chrom_strand", "consequence_allele_string",
    "consequence_type_tv", "ensembl_gene_stable_id", "ensembl_peptide_allele",
    "ensembl_transcript_stable_id", "ensembl_type", "minor_allele",
    "minor_allele_freq", "refsnp_id", "snp", "snp_allele",
    "snp_ensembl_aa_position", "snp_ensembl_peptide_allele",
)

_FILTERS = ("chr_name", "end", "start", "variation_source")


class NonHumanVariant(Variant):
    """Class to process a single non-human variant.

    This class receives a single variant and retrieves the related
    annotations, retrieving data from BioMart.

    Attributes:
        reference: reference allele
        position: nucleotide position
        alternate: alternate allele
        species: species to use for annotation

    Methods:
        response()
    """

    def __init__(self, reference, position, alternate, species):
        super().__init__(reference, position, alternate)
        self.species = species

    def response(self):
        """Retrieve the related information for the given variant.

        Results are converted to a dictionary by the .to_dict() method of
        the pandas dataframe returned. If no results are retrieved, the
        empty dict is returned.
        """
        resp = apy.query(attributes=["allele", "ensembl_gene_stable_id",
                                     "refsnp_id",
                                     "consequence_allele_string",
                                     "consequence_type_tv"],
                         filters={"chr_name": "MT",
                                  "start": str(self.position),
                                  "end": str(self.position)},
                         dataset=f"{self.species}_snp")
        resp.drop_duplicates("Variant alleles", inplace=True)

        # return resp.to_dict()
        return resp.to_dict(orient="records")


class NonHumanParser(Parser):
    """Class for a non-human variant parser.

    This class creates a single variant for each alternate allele found
    in a given vcf record, and associates it with the annotations
    determined by the input headers.

    Attributes:
        record: input vcf record
        headers: input vcf headers to which new annotations are added
        species: species to use for annotation

    Methods:
        parse()
    """

    def __init__(self, record, headers, species):
        super().__init__(record, headers)
        self.species = species

    def parse(self):
        """Parse response from NonHumanVariant and store them in the headers.

        If no results are retrieved a single . is returned.
        """
        variants = [NonHumanVariant(self.record.REF, self.record.POS, alt,
                                    self.species)
                    for alt in self.record.ALT]
        for variant in variants:
            response = variant.response()
            if len(response) > 0:
                for r in response:
                    for field in self.headers:
                        field.values = r.get(field.slug, ".")


class NonHumanAnnotator(Annotator):
    """Class for a non-human annotator.

    Attributes:
        input_vcf: input vcf file
        output_vcf: output vcf file
        species: species to use for annotation

    Methods:
        _update_header()
        _is_variation()
        _format_values()
        annotate()
        to_csv()
    """

    _HEADERS = (("Locus", "Gene stable ID",
                 "Locus to which the variant belongs"),
                ("dbSNP", "Variant name", "dbSNP ID of the variant"),
                ("Consequence", "Variant consequence",
                 "Functional effect of the variant"))

    def __init__(self, input_vcf, output_vcf, species):
        super().__init__(input_vcf, output_vcf, self._HEADERS)
        if species not in _SPECIES:
            raise ValueError("species not supported")
        self.species = species

    @staticmethod
    def _format_values(values):
        """Format entries returned by Field.values.

        Multiple entries are formatted as [entry1,entry2,entryN], single
        entries are formatted as entry1, empty values return a ..

        Args:
            values: entries in Field.values

        Returns:
            list with a single str element (as required by vcfpy)
        """
        values_set = sorted(set(values))
        if len(values_set) > 1:
            return [f"[{'|'.join(values_set)}]"]
        elif len(values_set) == 1:
            return [values_set.pop()]
        else:
            return ["."]

    def record_annotator(self, record):
        """Annotate a single record. Convenience function to be used with
        PoolExecutors.

        Args:
            record: input record to annotate
        """
        self._n_alleles.append(len(record.ALT))
        fields = [Field(head[0], head[1], head[2])
                  for head in self.headers]
        if self._is_variation(record):
            annots = NonHumanParser(record, fields, self.species)
            annots.parse()
            for field in fields:
                record.INFO[field.element] = self._format_values(field.values)
        return record

    def annotate(self):
        """Annotate variants found in the input vcf.

        An additional parsing is done by the _format_values() method, to
        write clean strings to the annotated vcf.
        """
        with ThreadPoolExecutor() as executor:
            for el in executor.map(self.record_annotator,
                                   [record for record in self._reader]):
                self._writer.write_record(el)

        self._reader.close()
        self._writer.close()

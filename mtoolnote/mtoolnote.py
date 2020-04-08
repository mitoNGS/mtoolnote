#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from mtoolnote.human import HumanAnnotator
from mtoolnote.nonhuman import NonHumanAnnotator


def annotate(input_vcf: str, output_vcf: str, species: str = "human",
             csv: bool = False,
             crossref: bool = True, predict: bool = True,
             variab: bool = True, haplos: bool = True):
    """Annotate an input VCF using mtoolnote.

    Args:
        input_vcf: input vcf file
        output_vcf: output vcf file
        species: species to use for annotation (default: 'human')
        csv: create an additional annotated CSV file (default: False)
        crossref: add cross-reference annotations (default: True)
        predict: add pathogenicity prediction annotations (default: True)
        variab: add nucleotide variability annotations (default: True)
        haplos: add haplogroup-specific allele frequency annotations
            (default: True)
    """
    if species == "human":
        vcf = HumanAnnotator(input_vcf, output_vcf,
                             crossref=crossref, predict=predict, variab=variab,
                             haplos=haplos)
    else:
        vcf = NonHumanAnnotator(input_vcf, output_vcf, species)

    vcf.annotate()

    if csv:
        vcf.to_csv()

    return

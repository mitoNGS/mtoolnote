#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from mtoolnote.human import HumanAnnotator
from mtoolnote.nonhuman import NonHumanAnnotator


def annotate(input_vcf: str, output_vcf: str, species: str = "human"):
    """Annotate an input VCF using mtoolnote.

    Args:
        input_vcf: input vcf file
        output_vcf: output vcf file
        species: species to use for annotation
    """
    if species == "human":
        vcf = HumanAnnotator(input_vcf, output_vcf)
    else:
        vcf = NonHumanAnnotator(input_vcf, output_vcf, species)

    vcf.annotate()

    return

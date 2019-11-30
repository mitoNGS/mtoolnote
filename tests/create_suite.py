#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import os
from mtoolnote import annotate


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
HUMAN = os.path.join(DATADIR, "human.vcf")
HUMAN_ANN = os.path.join(DATADIR, "human_ann.vcf")
GGALLUS = os.path.join(DATADIR, "ggallus.vcf")
GGALLUS_ANN = os.path.join(DATADIR, "ggallus_ann.vcf")


def main():
    """Create the test files needed."""
    click.echo("\n--- Human VCF test file ---\n")
    annotate(HUMAN, HUMAN_ANN, csv=True)
    click.echo("\tAnnotation complete.")
    click.echo("\n--- GGallus VCF test file ---\n")
    annotate(GGALLUS, GGALLUS_ANN, "ggallus", csv=True)
    click.echo("\tAnnotation complete.")


if __name__ == '__main__':
    main()

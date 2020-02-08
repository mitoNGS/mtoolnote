#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import os
from mtoolnote import annotate
from mtoolnote.tests.constants import HUMAN, HUMAN_ANN, GGALLUS, GGALLUS_ANN


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

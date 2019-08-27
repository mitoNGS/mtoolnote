#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import sys
import click
from mtoolnote.classes import _SPECIES
from mtoolnote.human import HumanAnnotator
from mtoolnote.nonhuman import NonHumanAnnotator


@click.command()
@click.version_option()
@click.argument("input_vcf")
@click.argument("output_vcf")
@click.option("--species", "-s", default="human",
              type=click.Choice(("human", ) + _SPECIES),
              help="Species to use for annotation (default: human)")
def main(input_vcf, output_vcf, species):
    """Annotate a VCF file using mtoolnote."""
    if species == "human":
        vcf = HumanAnnotator(input_vcf, output_vcf)
    else:
        vcf = NonHumanAnnotator(input_vcf, output_vcf, species)
    click.echo(f"Annotating {input_vcf} (species {species})... ", nl=False)
    vcf.annotate()
    click.echo("Done.")
    click.echo(f"Annotated VCF is saved to {output_vcf}.")

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

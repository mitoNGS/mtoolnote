#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import sys

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
@click.option("--csv", "-c", is_flag=True, default=False,
              help="Create an additional annotated CSV file (default: False)")
def main(input_vcf, output_vcf, species, csv):
    """Annotate a VCF file using mtoolnote."""
    if species == "human":
        vcf = HumanAnnotator(input_vcf, output_vcf)
    else:
        vcf = NonHumanAnnotator(input_vcf, output_vcf, species)

    click.echo(f"Annotating {input_vcf} (species {species})... ", nl=False)
    vcf.annotate()
    click.echo("Done.")
    click.echo(f"Annotated VCF is saved to {output_vcf}.")

    if csv:
        click.echo("Converting annotated VCF file to CSV format... ", nl=False)
        vcf.to_csv()
        click.echo("Done.")

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

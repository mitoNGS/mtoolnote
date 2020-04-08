#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import sys

from mtoolnote.constants import SPECIES
from mtoolnote.human import HumanAnnotator
from mtoolnote.nonhuman import NonHumanAnnotator


@click.command()
@click.version_option()
@click.argument("input_vcf")
@click.argument("output_vcf")
@click.option("--species", "-s", default="human", show_default=True,
              type=click.Choice(("human", ) + SPECIES),
              help="Species to use for annotation")
@click.option("--csv", "-c", is_flag=True, default=False, show_default=True,
              help="Create an additional annotated CSV file")
@click.option("--crossref/--no-crossref", default=True, show_default=True,
              help="Add cross-reference annotations")
@click.option("--predict/--no-predict", default=True, show_default=True,
              help="Add pathogenicity prediction annotations")
@click.option("--variab/--no-variab", default=True, show_default=True,
              help="Add nucleotide variability annotations")
@click.option("--haplos/--no-haplos", default=True, show_default=True,
              help="Add haplogroup-specific allele frequency annotations")
def main(input_vcf, output_vcf, species, csv, crossref, predict, variab,
         haplos):
    """Annotate a VCF file using mtoolnote."""
    if species == "human":
        vcf = HumanAnnotator(input_vcf, output_vcf, crossref=crossref,
                             predict=predict, variab=variab, haplos=haplos)
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

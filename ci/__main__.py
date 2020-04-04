#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
from pkg_resources import resource_filename
import shutil
import subprocess

import click
import pandas as pd
from sqlalchemy import create_engine

from mtoolnote.models import Base
from mtoolnote.mtoolnote import annotate
from mtoolnote.tests.constants import HUMAN, HUMAN_ANN, GGALLUS, GGALLUS_ANN


@click.group()
def cli():
    """ Main entry point for the CI infrastructure. """
    pass


@cli.command(name="build")
def build():
    """ Build the package to be uploaded to PyPI. """
    build_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                             "build")
    dist_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            "dist")
    eggs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                            ".eggs")
    egg_info_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "mitoviz.egg-info")

    if os.path.isdir(build_dir):
        click.echo("Removing build directory... ", nl=False)
        shutil.rmtree(build_dir)
        click.echo("Done.")

    if os.path.isdir(eggs_dir):
        click.echo("Removing .eggs directory... ", nl=False)
        shutil.rmtree(eggs_dir)
        click.echo("Done.")

    if os.path.isdir(egg_info_dir):
        click.echo("Removing .egg-info directory... ", nl=False)
        shutil.rmtree(egg_info_dir)
        click.echo("Done.")

    if os.path.isdir(dist_dir):
        click.echo("Removing dist directory... ", nl=False)
        shutil.rmtree(dist_dir)
        click.echo("Done.")

    click.echo("Building package...")
    subprocess.check_call(["python", "setup.py", "sdist", "bdist_wheel"])
    click.echo("Done.")


@cli.command(name="create-db")
def create_db():
    dbfile = resource_filename("mtoolnote", "data/mtoolnote.db")
    engine = create_engine(f"sqlite:///{dbfile}")
    click.echo(f"Creating {dbfile}... ", nl=False)
    Base.metadata.create_all(bind=engine)
    click.echo("Done.")


@cli.command(name="create-suite")
def create_suite():
    """ Create all files needed for testing. """
    click.echo("Updating test files...")

    click.echo("\n--- Human VCF/CSV test files ---\n")
    annotate(HUMAN, HUMAN_ANN, csv=True)
    click.echo("\tAnnotation complete.")

    click.echo("\n--- Ggallus VCF/CSV test files ---\n")
    annotate(GGALLUS, GGALLUS_ANN, "ggallus", csv=True)
    click.echo("\tAnnotation complete.")

    click.echo("Done.")


@cli.command(name="docs")
def docs():
    """ Create documentation. """
    click.echo("Creating documentation with Sphinx...")
    subprocess.check_call(
        ["sphinx-build", "-b", "html", "docs", "docs/_build"]
    )
    click.echo("Done.")


@cli.command(name="flake8")
def flake8():
    """ Perform flake8 checks on the code. """
    click.echo("Performing flake8 linting...")
    subprocess.check_call(["flake8", "mitoviz"])
    click.echo("Done.")


@cli.command(name="install")
def install():
    """ Install the package (in development mode). """
    click.echo("Installing mitoviz...")
    subprocess.check_call(["pip", "install", "-e", "."])
    click.echo("Done.")


@cli.command(name="install-reqs")
def install_reqs():
    """ Install all requirements needed for the package. """
    click.echo(
        "Installing requirements for mitoviz..."
    )
    subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    click.echo("Done.")


@cli.command(name="update-db")
def update_db():
    dbfile = resource_filename("mtoolnote", "data/mtoolnote.db")
    engine = create_engine(f"sqlite:///{dbfile}")
    click.echo("Updating database tables...")

    sources = ("Main", "CrossRef", "FuncLoci", "Loci", "Plasmy",
               "Predict", "Variab", "Annot")
    for source in sources:
        tablefile = resource_filename("mtoolnote",
                                      f"data/tables/{source}.csv")
        click.echo(f"\tUpdating {source} table... ", nl=False)
        df = pd.read_csv(tablefile, na_values="<null>")
        df.reset_index(inplace=True)
        df.rename(columns={"index": "id"}, inplace=True)
        with engine.connect() as conn:
            df.to_sql(name=source, con=conn, index=False,
                      if_exists="replace", index_label="id")
        click.echo("Complete.")

    haplos = ("Haplo_A", "Haplo_B", "Haplo_D", "Haplo_G",
              "Haplo_JT", "Haplo_L0", "Haplo_L1", "Haplo_L2",
              "Haplo_L3_star", "Haplo_L4", "Haplo_L5", "Haplo_L6",
              "Haplo_M7", "Haplo_M8", "Haplo_M9",
              "Haplo_M_star", "Haplo_N1", "Haplo_N2", "Haplo_N9",
              "Haplo_N_star", "Haplo_R0", "Haplo_R9",
              "Haplo_R_star", "Haplo_U", "Haplo_X")
    for haplo in haplos:
        tablefile = resource_filename("mtoolnote",
                                      f"data/tables/{haplo}.csv")
        click.echo(f"\tUpdating {haplo} table... ", nl=False)
        df = pd.read_csv(tablefile, na_values="<null>",
                         names=["position", "freq_A", "freq_C",
                                "freq_G", "freq_T", "freq_gap",
                                "freq_oth"],
                         skiprows=1)
        df.reset_index(inplace=True)
        df.rename(columns={"index": "id"}, inplace=True)
        with engine.connect() as conn:
            df.to_sql(name=haplo, con=conn, index=False,
                      if_exists="replace", index_label="id")
        click.echo("Complete.")

    click.echo("Done.")


@cli.command(name="check")
def twine_check():
    """ Check the package using Twine. """
    click.echo("Checking package...")
    subprocess.check_call(["twine", "check", "dist/*"])
    click.echo("Done.")


@cli.command(name="upload")
@click.option("-u", "--username", default=None, help="PyPI username.")
@click.option("-p", "--password", default=None, help="PyPI password.")
def twine_upload(username, password):
    """ Upload the package to PyPI using Twine.
    Args:
        username: PyPI username (if not provided, twine will ask for it)
        password: PyPI password (if not provided, twine will ask for it)
    """
    cmd = ["twine", "upload"]
    if username:
        cmd.extend(["-u", username])
        if password:
            cmd.extend(["-p", password])
    cmd.append("dist/*")

    click.echo("Uploading package...")
    subprocess.check_call(cmd)
    click.echo("Done.")


if __name__ == '__main__':
    cli()

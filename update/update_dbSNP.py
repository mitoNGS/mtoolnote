#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import click
import json
import pandas as pd
import requests

from mtoolnote.models import CrossRef, Main


def get_dbsnp_id(pos: int, ref: str, alt: str) -> str:
    """ Collect the dbSNP id for a given variant, using dbSNP's API.

    Args:
        pos: position of the variant
        ref: reference allele of the variant
        alt: alternate allele of the variant

    Returns:
        dbSNP id of the given variant, if found, or empty string otherwise
    """
    url = "https://api.ncbi.nlm.nih.gov/variation/v0/spdi/{}/rsids"
    variant = "NC_012920.1:{}:{}:{}"
    if alt == "d":  # deletions
        variant = variant.format(pos, ref, "")
    elif alt.startswith("."):  # insertions
        variant = variant.format(pos, "", alt.strip("."))
    else:
        variant = variant.format(pos, ref, alt)

    resp = requests.get(url.format(variant))
    resp_json = resp.json()

    try:
        dbsnp_id = resp_json["data"]["rsids"][0]
    except KeyError:
        dbsnp_id = ""
    return dbsnp_id


def main():
    main_df = pd.read_csv("Main.csv", na_values="<null>")
    main_df.set_index("id", inplace=True)
    cross_df = pd.read_csv("CrossRef.csv", na_values="<null>")
    cross_df.set_index("id", inplace=True)
    refsnps = {}

    for row in main_df.itertuples():
        click.echo(f"Searching {row.nt_start} {row.ref_rCRS} {row.alt}... ",
                   nl=False)
        if row.nt_start in refsnps:
            click.echo("Defaulting to cached value.")
            cross_df.at[row.Index, "dbSNP"] = f"rs{refsnps[row.nt_start]}"
            continue
        dbsnp_id = get_dbsnp_id((row.nt_start-1), row.ref_rCRS, row.alt)
        if dbsnp_id != "":
            cross_df.at[row.Index, "dbSNP"] = f"rs{dbsnp_id}"
            click.echo(dbsnp_id)
            refsnps[row.nt_start] = dbsnp_id
        else:
            click.echo("")

    cross_df.reset_index(inplace=True)
    cross_df.to_csv("new_CrossRef.csv", index=False, na_rep="<null>")


if __name__ == '__main__':
    main()

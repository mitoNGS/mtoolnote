#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os
from click.testing import CliRunner
from mtoolnote import cli, annotate


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
HUMAN = os.path.join(DATADIR, "human.vcf")
HUMAN_ANN = os.path.join(DATADIR, "human_ann.vcf")
HUMAN_ANN_CSV = os.path.join(DATADIR, "human_ann.csv")
GGALLUS = os.path.join(DATADIR, "ggallus.vcf")
GGALLUS_ANN = os.path.join(DATADIR, "ggallus_ann.vcf")
GGALLUS_ANN_CSV = os.path.join(DATADIR, "ggallus_ann.csv")
TEST_VCF = os.path.join(DATADIR, "test.vcf")
TEST_CSV = os.path.join(DATADIR, "test.csv")


# module

def test_annotate_human(human_ann_vcf, human_ann_csv):
    """Test human annotation using mtoolnote.annotate()."""
    annotate(HUMAN, TEST_VCF, csv=True)
    with open(TEST_VCF) as result:
        assert result.read() == human_ann_vcf.read()
    with open(TEST_CSV) as result_csv: 
        assert result_csv.read() == human_ann_csv.read()


def test_annotate_ggallus(ggallus_ann_vcf, ggallus_ann_csv):
    """Test ggallus annotation using mtoolnote.annotate()."""
    annotate(GGALLUS, TEST_VCF, "ggallus", csv=True)
    with open(TEST_VCF) as result:
        assert result.read() == ggallus_ann_vcf.read()
    with open(TEST_CSV) as result_csv: 
        assert result_csv.read() == ggallus_ann_csv.read()


# cli

def test_cli_help():
    """Test the CLI help."""
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--help'])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


def test_annotate_human_cli(human_ann_vcf, human_ann_csv):
    """Test human annotation using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [HUMAN, TEST_VCF, "-c"])
    assert result.exit_code == 0
    with open(TEST_VCF) as ann_test:
        assert ann_test.read() == human_ann_vcf.read()
    with open(TEST_CSV) as result_csv: 
        assert result_csv.read() == human_ann_csv.read()


def test_annotate_ggallus_cli(ggallus_ann_vcf, ggallus_ann_csv):
    """Test ggallus annotation using the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [GGALLUS, TEST_VCF, 
                                      "--species", "ggallus", "-c"])
    assert result.exit_code == 0
    with open(TEST_VCF) as ann_test:
        assert ann_test.read() == ggallus_ann_vcf.read()
    with open(TEST_CSV) as result_csv: 
        assert result_csv.read() == ggallus_ann_csv.read()

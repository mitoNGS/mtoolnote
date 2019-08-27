#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
HUMAN = os.path.join(DATADIR, "human.vcf")
HUMAN_ANN = os.path.join(DATADIR, "human_ann.vcf")
GGALLUS = os.path.join(DATADIR, "ggallus.vcf")
GGALLUS_ANN = os.path.join(DATADIR, "ggallus_ann.vcf")


@pytest.fixture
def human_vcf():
    """Open the human vcf."""
    with open(HUMAN) as f:
        yield f


@pytest.fixture
def human_ann_vcf():
    """Open the annotated human vcf."""
    with open(HUMAN_ANN) as f:
        yield f


@pytest.fixture
def ggallus_vcf():
    """Open the ggallus vcf."""
    with open(GGALLUS) as f:
        yield f


@pytest.fixture
def ggallus_ann_vcf():
    """Open the annotated ggallus vcf."""
    with open(GGALLUS_ANN) as f:
        yield f

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import pytest
import os

from mtoolnote.tests.constants import (
    HUMAN, HUMAN_ANN, HUMAN_ANN_CSV, HUMAN_ANN_HAPLOS, HUMAN_ANN_HAPLOS_CSV,
    GGALLUS, GGALLUS_ANN, GGALLUS_ANN_CSV
)


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
def human_ann_csv():
    """Open the annotated human csv."""
    with open(HUMAN_ANN_CSV) as f:
        yield f


@pytest.fixture
def human_ann_haplos_vcf():
    """Open the haplos annotated human vcf."""
    with open(HUMAN_ANN_HAPLOS) as f:
        yield f


@pytest.fixture
def human_ann_haplos_csv():
    """Open the haplos annotated human csv."""
    with open(HUMAN_ANN_HAPLOS_CSV) as f:
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


@pytest.fixture
def ggallus_ann_csv():
    """Open the annotate ggallus csv."""
    with open(GGALLUS_ANN_CSV) as f:
        yield f

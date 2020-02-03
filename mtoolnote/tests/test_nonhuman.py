#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest

import pandas as pd

from mtoolnote.classes import Field
from mtoolnote.nonhuman import NonHumanAnnotator, NonHumanVariant

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
GGALLUS = os.path.join(DATADIR, "ggallus.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")

apy_query_result = pd.DataFrame({'Variant alleles': {0: 'C/T',
  1: 'C/T',
  2: 'C/T',
  3: 'C/T',
  4: 'C/T',
  5: 'C/T',
  6: 'C/T',
  7: 'C/T'},
 'Gene stable ID': {0: 'ENSGALG00000032059',
  1: 'ENSGALG00000035975',
  2: 'ENSGALG00000041922',
  3: 'ENSGALG00000043598',
  4: 'ENSGALG00000036956',
  5: 'ENSGALG00000040296',
  6: 'ENSGALG00000029193',
  7: 'ENSGALG00000042750'},
 'Variant name': {0: 'rs1060378625',
  1: 'rs1060378625',
  2: 'rs1060378625',
  3: 'rs1060378625',
  4: 'rs1060378625',
  5: 'rs1060378625',
  6: 'rs1060378625',
  7: 'rs1060378625'},
 'Consequence specific allele': {0: 'C/T',
  1: 'C/T',
  2: 'C/T',
  3: 'C/T',
  4: 'C/T',
  5: 'C/T',
  6: 'C/T',
  7: 'C/T'},
 'Variant consequence': {0: 'upstream_gene_variant',
  1: 'upstream_gene_variant',
  2: 'upstream_gene_variant',
  3: 'upstream_gene_variant',
  4: 'upstream_gene_variant',
  5: 'upstream_gene_variant',
  6: 'downstream_gene_variant',
  7: 'upstream_gene_variant'}})


class TestNonHumanVariant(unittest.TestCase):

    def setUp(self) -> None:
        self.variant = NonHumanVariant("C", 164, "T", "ggallus")




class TestNonHumanAnnotator(unittest.TestCase):

    def setUp(self) -> None:
        self.annot = NonHumanAnnotator(
            input_vcf=GGALLUS,
            output_vcf=TEST_VCF,
            species="ggallus"
        )

        self.field = Field(
            element="Tester",
            slug="tester",
            description="Tester element",
        )

    def test__format_values(self):
        # Given
        values = ["0.1", "1", "0.5", "0.7", "."]
        expected = ["[.|0.1|0.5|0.7|1]"]
        for value in values:
            self.field.values = value

        # When
        result = self.annot._format_values(self.field.values)

        # Then
        self.assertEqual(expected, result)

    def test__format_values_single(self):
        # Given
        value = "0.5"
        expected = ["0.5"]
        self.field.values = value

        # When
        result = self.annot._format_values(self.field.values)

        # Then
        self.assertEqual(expected, result)

    def test__format_values_empty(self):
        # Given
        expected = ["."]

        # When
        result = self.annot._format_values(self.field.values)

        # Then
        self.assertEqual(expected, result)


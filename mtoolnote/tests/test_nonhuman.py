#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os
import unittest
from unittest.mock import Mock, patch

import pandas as pd
import pandas.testing as pdt

from mtoolnote.classes import Field
from mtoolnote.nonhuman import NonHumanAnnotator, NonHumanVariant
from mtoolnote.tests.constants import GGALLUS, TEST_VCF

apy_query_result = pd.DataFrame({
    'Variant alleles': {
        0: 'C/T',
        1: 'C/T',
        2: 'C/T',
        3: 'C/T',
        4: 'C/T',
        5: 'C/T',
        6: 'C/T',
        7: 'C/T'
    },
    'Gene stable ID': {
        0: 'ENSGALG00000032059',
        1: 'ENSGALG00000035975',
        2: 'ENSGALG00000041922',
        3: 'ENSGALG00000043598',
        4: 'ENSGALG00000036956',
        5: 'ENSGALG00000040296',
        6: 'ENSGALG00000029193',
        7: 'ENSGALG00000042750'
    },
    'Variant name': {
        0: 'rs1060378625',
        1: 'rs1060378625',
        2: 'rs1060378625',
        3: 'rs1060378625',
        4: 'rs1060378625',
        5: 'rs1060378625',
        6: 'rs1060378625',
        7: 'rs1060378625'
    },
    'Consequence specific allele': {
        0: 'C/T',
        1: 'C/T',
        2: 'C/T',
        3: 'C/T',
        4: 'C/T',
        5: 'C/T',
        6: 'C/T',
        7: 'C/T'},
    'Variant consequence': {
        0: 'upstream_gene_variant',
        1: 'upstream_gene_variant',
        2: 'upstream_gene_variant',
        3: 'upstream_gene_variant',
        4: 'upstream_gene_variant',
        5: 'upstream_gene_variant',
        6: 'downstream_gene_variant',
        7: 'upstream_gene_variant'
    }
})


class TestNonHumanVariant(unittest.TestCase):

    def setUp(self) -> None:
        self.variant = NonHumanVariant("C", 164, "T", "ggallus")

    def test_variant(self):
        # Given
        expected = {
            "Variant alleles": "C/T",
            "Gene stable ID": "ENSGALG00000032059",
            "Variant name": "rs1060378625",
            "Consequence specific allele": "C/T",
            "Variant consequence": "upstream_gene_variant",
        }

        with patch("apybiomart.query") as apy_query:
            apy_query.return_value = apy_query_result
            self.assertEqual(
                expected,
                self.variant.response()[0]
            )


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


#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import namedtuple
import os
import unittest
from unittest.mock import Mock, patch

from mtoolnote.classes import Field, Variant, Annotator
from mtoolnote.constants import NONHUMAN_HEADERS

DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
GGALLUS = os.path.join(DATADIR, "ggallus.vcf")
TEST_VCF = os.path.join(DATADIR, "test.vcf")


class TestField(unittest.TestCase):

    def setUp(self) -> None:
        self.field = Field(
            element="Tester",
            slug="tester",
            description="Tester element",
        )

    def test__replace_null(self):
        # Given
        value = "test"

        # When
        result = self.field._replace_null(value)

        # Then
        self.assertEqual(value, result)

        # Given
        value = None

        # When
        result = self.field._replace_null(value)

        # Then
        self.assertEqual(".", result)

    def test_values(self):
        # Given/When/Then
        self.assertEqual([], self.field.values)

        # Given
        values = ["t", 1, 0.5, None, "."]
        expected = ["t", 1, 0.5, ".", "."]

        # When
        for value in values:
            self.field.values = value

        # Then
        self.assertEqual(expected, self.field.values)


class TestVariant(unittest.TestCase):

    @patch.object(Variant, '__abstractmethods__', set())
    def setUp(self) -> None:
        self.alternate_tup = namedtuple(
            "Alternate",
            "type"
        )

        self.deletion_alt = self.alternate_tup(type="DEL")
        self.insertion_alt = self.alternate_tup(type="INS")
        self.snp_alt = self.alternate_tup(type="SNP")

        self.insertion_var = Variant(
            reference="G",
            position=69,
            alternate=self.insertion_alt,
        )

        self.deletion_var = Variant(
            reference="A",
            position=420,
            alternate=self.deletion_alt,
        )

        self.snp_var = Variant(
            reference="C",
            position=5,
            alternate=self.snp_alt,
        )

    def test__is_insertion(self):
        # Given/When
        expected_ins = self.insertion_var._is_insertion()
        expected_del = self.deletion_var._is_insertion()
        expected_snp = self.snp_var._is_insertion()

        # Then
        self.assertTrue(expected_ins)
        self.assertFalse(expected_del)
        self.assertFalse(expected_snp)

    def test__is_deletion(self):
        # Given/When
        expected_del = self.deletion_var._is_deletion()
        expected_ins = self.insertion_var._is_deletion()
        expected_snp = self.snp_var._is_deletion()

        # Then
        self.assertTrue(expected_del)
        self.assertFalse(expected_ins)
        self.assertFalse(expected_snp)


class TestAnnotator(unittest.TestCase):

    @patch.object(Annotator, '__abstractmethods__', set())
    def setUp(self) -> None:
        self.annot = Annotator(input_vcf=GGALLUS,
                               output_vcf=TEST_VCF,
                               headers=NONHUMAN_HEADERS)

    def test__is_variation_valid(self):
        # Given/When
        record = Mock()
        record.ALT = [Mock(), Mock()]
        record.ALT[0].value = "A"
        record.ALT[1].value = "G"

        # Then
        self.assertTrue(
            self.annot._is_variation(record)
        )

    def test__is_variation_empty(self):
        # Given/When
        record = Mock()
        record.ALT = []

        # Then
        self.assertFalse(
            self.annot._is_variation(record)
        )

    def test__is_variation_invalid(self):
        # Given/When
        record = Mock()
        record.ALT = [Mock(), Mock()]
        record.ALT[0].value = "."
        record.ALT[1].value = "G"

        # Then
        self.assertFalse(
            self.annot._is_variation(record)
        )

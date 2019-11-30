#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import namedtuple
import unittest
from unittest.mock import patch

from mtoolnote.classes import Field, Variant


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
        self.assertEqual(result, value)

        # Given
        value = None

        # When
        result = self.field._replace_null(value)

        # Then
        self.assertEqual(result, ".")

    def test_values(self):
        # Given
        values = ["t", 1, 0.5, None, "."]
        expected = ["t", 1, 0.5, ".", "."]

        # When
        for value in values:
            self.field.values = value

        # Then
        self.assertEqual(self.field.values, expected)


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
        expected_true = self.insertion_var._is_insertion()
        expected_false1 = self.deletion_var._is_insertion()
        expected_false2 = self.snp_var._is_insertion()

        # Then
        self.assertEqual(expected_true, True)
        self.assertEqual(expected_false1, False)
        self.assertEqual(expected_false2, False)

    def test__is_deletion(self):
        # Given/When
        expected_true = self.deletion_var._is_deletion()
        expected_false1 = self.insertion_var._is_deletion()
        expected_false2 = self.snp_var._is_deletion()

        # Then
        self.assertEqual(expected_true, True)
        self.assertEqual(expected_false1, False)
        self.assertEqual(expected_false2, False)



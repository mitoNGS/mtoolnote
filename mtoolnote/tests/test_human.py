#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import namedtuple
import unittest
from unittest.mock import Mock, patch

from mtoolnote.human import HumanVariant


class TestHumanVariant(unittest.TestCase):

    def setUp(self) -> None:
        self.alternate_tup = namedtuple("Alternate", "type value")
        self.snp_alt = self.alternate_tup(type="SNP", value="T")

        self.session = Mock()
        self.variant = HumanVariant("C", 3000, self.snp_alt, self.session)

    def test__locus(self):
        # Given
        expected = "RNR2"

        # When
        result = self.variant._locus

        # Then
        self.assertEqual(expected, result)

    def test_response(self):
        # Given
        expected = {
            "nt_start": 3000,
            "ref_rCRS": "C",
            "alt": self.snp_alt,
            "nt_end": 3000,
            "locus": "RNR2"
        }

        # When
        with patch("mtoolnote.human.HumanVariant._snp_query") as query:
            query.return_value = None
            result = self.variant.response()

        # Then
        self.assertEqual(expected, result)
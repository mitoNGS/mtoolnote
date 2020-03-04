#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from collections import namedtuple
from pkg_resources import resource_filename
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from mtoolnote.human import HumanVariant


class TestHumanVariant(unittest.TestCase):

    def setUp(self) -> None:
        self.alternate_tup = namedtuple("Alternate", "type value")
        self.snp_alt = self.alternate_tup(type="SNP", value="T")

        _dbfile = resource_filename(__name__, "../data/hmtvar.db")
        engine = create_engine(f"sqlite:///{_dbfile}")
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.variant = HumanVariant("C", 3000, self.snp_alt, self.session)

    def test__locus(self):
        # Given
        expected = "MT-RNR2 (16S Ribosomal RNA)"

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
            "locus": "MT-RNR2 (16S Ribosomal RNA)"
        }

        # When
        result = self.variant.response()

        # Then
        self.assertEqual(expected, result)

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
import os


DATADIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
HUMAN = os.path.join(DATADIR, "human.vcf")
HUMAN_ANN = os.path.join(DATADIR, "human_ann.vcf")
HUMAN_ANN_CSV = os.path.join(DATADIR, "human_ann.csv")
HUMAN_ANN_HAPLOS = os.path.join(DATADIR, "human_ann_haplos.vcf")
HUMAN_ANN_HAPLOS_CSV = os.path.join(DATADIR, "human_ann_haplos.csv")
GGALLUS = os.path.join(DATADIR, "ggallus_single.vcf")
GGALLUS_ANN = os.path.join(DATADIR, "ggallus_ann_single.vcf")
GGALLUS_ANN_CSV = os.path.join(DATADIR, "ggallus_ann_single.csv")
TEST_VCF = os.path.join(DATADIR, "test.vcf")
TEST_CSV = os.path.join(DATADIR, "test.csv")

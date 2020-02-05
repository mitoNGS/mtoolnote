#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste

HEADERS_MAIN = (
    ("Locus", "locus", "Locus to which the variant belongs"),
    ("CodonPosition", "codon_position", "Codon position of the variant"),
    ("AaChange", "aa_change", "Aminoacidic change determined"),
    ("Pathogenicity", "pathogenicity", "Pathogenicity predicted by HmtVar"))

HEADERS_CROSSREF = (
    ("Clinvar", "clinvar", "Clinvar ID of the variant"),
    ("dbSNP", "dbSNP", "dbSNP ID of the variant"),
    ("OMIM", "omim", "OMIM ID of the variant"),
    # ("MitomapAssociatedDiseases", "mitomap_associated_disease",
    #  "Diseases associated to the variant according to Mitomap"),
    # ("MitomapSomaticMutations", "somatic_mutations",
    #  "Diseases associated to the variant according to Mitomap Somatic Mutations"),
    # ("MitomapHeteroplasmy", "mitomap_hetero",
    #  "The variant was found as heteroplasmic in Mitomap datasets (Y=yes,N=no)"),
    # ("MitomapHomoplasmy", "mitomap_homo",
    #  "The variant was found as homoplasmic in Mitomap datasets (Y=yes,N=no)"),
    # ("SomaticMutationsHeteroplasmy", "sm_hetero",
    #  "The variant was found as heteroplasmic in Mitomap Somatic Mutations datasets (Y=yes,N=no)"),
    # ("SomaticMutationsHomoplasmy", "sm_homo",
    #  "The variant was found as homoplasmic in Mitomap Somatic Mutations datasets (Y=yes,N=no)"),
    # ("1KGenomesHeteroplasmy", "genomes1K_hetero",
    #  "The variant was found as heteroplasmic in 1KGenomes datasets (Y=yes,N=no)"),
    # ("1KGenomesHomoplasmy", "genomes1K_homo",
    #  "The variant was found as homoplasmic in 1KGenomes datasets (Y=yes,N=no)")
)

HEADER_PREDICT = (
    ("MutPred_Prediction", "mutPred_pred",
     "Pathogenicity prediction offered by MutPred"),
    ("MutPred_Probability", "mutPred_prob",
     "Confidence of the pathogenicity prediction offered by MutPred"),
    ("Panther_Prediction", "panther_pred",
     "Pathogenicity prediction offered by Panther"),
    ("Panther_Probability", "panther_prob",
     "Confidence of the pathogenicity prediction offered by Panther"),
    ("PhDSNP_Prediction", "phD_snp_pred",
     "Pathogenicity prediction offered by PhD SNP"),
    ("PhDSNP_Probability", "phD_snp_prob",
     "Confidence of the pathogenicity prediction offered by PhD SNP"),
    ("SNPsGO_Prediction", "snp_go_pred",
     "Pathogenicity prediction offered by SNPs & GO"),
    ("SNPsGO_Probability", "snp_go_prob",
     "Confidence of the pathogenicity prediction offered by SNPs & GO"),
    ("Polyphen2HumDiv_Prediction", "polyphen2_humDiv_pred",
     "Pathogenicity prediction offered by Polyphen2 HumDiv"),
    ("Polyphen2HumDiv_Probability", "polyphen2_humDiv_prob",
     "Confidence of the pathogenicity prediction offered by Polyphen2 HumDiv"),
    ("Polyphen2HumVar_Prediction", "polyphen2_humVar_pred",
     "Pathogenicity prediction offered by Polyphen2 HumVar"),
    ("Polyphen2HumVar_Probability", "polyphen2_humVar_prob",
     "Confidence of the pathogenicity prediction offered by Polyphen2 HumVar")
)

HEADERS_VARIAB = (
    ("NtVarH", "nt_var",
     "Nucleotide variability of the position in healthy individuals"),
    ("NtVarP", "nt_var_patients",
     "Nucleotide variability of the position in patient individuals"),
    ("AaVarH", "aa_var",
     "Aminoacid variability of the position in healthy individuals"),
    ("AaVarP", "aa_var_patients",
     "Aminoacid variability of the position in patient individuals"),
    # ("AlleleFreqH", "all_freq_h",
    #  "Allele frequency of the variant in healthy individuals overall"),
    # ("AlleleFreqP", "all_freq_p",
    #  "Allele frequency of the variant in patient individuals overall"),
    # ("AlleleFreqH_AF", "all_freq_h_AF",
    #  "Allele frequency of the variant in healthy individuals from Africa"),
    # ("AlleleFreqP_AF", "all_freq_p_AF",
    #  "Allele frequency of the variant in patient individuals from Africa"),
    # ("AlleleFreqH_AM", "all_freq_h_AM",
    #  "Allele frequency of the variant in healthy individuals from America"),
    # ("AlleleFreqP_AM", "all_freq_p_AM",
    #  "Allele frequency of the variant in patient individuals from America"),
    # ("AlleleFreqH_AS", "all_freq_h_AS",
    #  "Allele frequency of the variant in healthy individuals from Asia"),
    # ("AlleleFreqP_AS", "all_freq_p_AS",
    #  "Allele frequency of the variant in patient individuals from Asia"),
    # ("AlleleFreqH_EU", "all_freq_h_EU",
    #  "Allele frequency of the variant in healthy individuals from Europe"),
    # ("AlleleFreqP_EU", "all_freq_p_EU",
    #  "Allele frequency of the variant in patient individuals from Europe"),
    # ("AlleleFreqH_OC", "all_freq_h_OC",
    #  "Allele frequency of the variant in healthy individuals from Oceania"),
    # ("AlleleFreqP_OC", "all_freq_p_OC",
    #  "Allele frequency of the variant in patient individuals from Oceania")
)

HEADERS_HAPLOS = (
    ("Haplo_A", "Haplo_A", "Allele frequency of the variant in haplogroup A"),
    ("Haplo_B", "Haplo_B", "Allele frequency of the variant in haplogroup B"),
    ("Haplo_D", "Haplo_D", "Allele frequency of the variant in haplogroup D"),
    ("Haplo_G", "Haplo_G", "Allele frequency of the variant in haplogroup G"),
    ("Haplo_JT", "Haplo_JT", "Allele frequency of the variant in haplogroup JT"),
    ("Haplo_L0", "Haplo_L0", "Allele frequency of the variant in haplogroup L0"),
    ("Haplo_L1", "Haplo_L1", "Allele frequency of the variant in haplogroup L1"),
    ("Haplo_L2", "Haplo_L2", "Allele frequency of the variant in haplogroup L2"),
    ("Haplo_L3*", "Haplo_L3_star", "Allele frequency of the variant in haplogroup L3*"),
    ("Haplo_L4", "Haplo_L4", "Allele frequency of the variant in haplogroup L4"),
    ("Haplo_L5", "Haplo_L5", "Allele frequency of the variant in haplogroup L5"),
    ("Haplo_L6", "Haplo_L6", "Allele frequency of the variant in haplogroup L6"),
    ("Haplo_M7", "Haplo_M7", "Allele frequency of the variant in haplogroup M7"),
    ("Haplo_M8", "Haplo_M8", "Allele frequency of the variant in haplogroup M8"),
    ("Haplo_M9", "Haplo_M9", "Allele frequency of the variant in haplogroup M9"),
    ("Haplo_M*", "Haplo_M_star", "Allele frequency of the variant in haplogroup M*"),
    ("Haplo_N1", "Haplo_N1", "Allele frequency of the variant in haplogroup N1"),
    ("Haplo_N2", "Haplo_N2", "Allele frequency of the variant in haplogroup N2"),
    ("Haplo_N9", "Haplo_N9", "Allele frequency of the variant in haplogroup N9"),
    ("Haplo_N*", "Haplo_N_star", "Allele frequency of the variant in haplogroup N*"),
    ("Haplo_R0", "Haplo_R0", "Allele frequency of the variant in haplogroup R0"),
    ("Haplo_R9", "Haplo_R9", "Allele frequency of the variant in haplogroup R9"),
    ("Haplo_R*", "Haplo_R_star", "Allele frequency of the variant in haplogroup R*"),
    ("Haplo_U", "Haplo_U", "Allele frequency of the variant in haplogroup U"),
    ("Haplo_X", "Haplo_X", "Allele frequency of the variant in haplogroup X"),
)

HUMAN_HEADERS = (*HEADERS_MAIN, *HEADER_PREDICT, *HEADERS_VARIAB,
                 *HEADERS_CROSSREF, *HEADERS_HAPLOS)

MT_POS_DICT = {"TF": range(576, 647),
               "RNR1": range(647, 1601),
               "TV": range(1601, 1670),
               "RNR2": range(1670, 3229),
               "TL1": range(3229, 3304),
               "ND1": range(3304, 4262),
               "TI": range(4262, 4331),
               "TQ": range(4331, 4400),
               "TM": range(4400, 4469),
               "ND2": range(4469, 5511),
               "TW": range(5511, 5579),
               "TA": range(5579, 5655),
               "TN": range(5655, 5729),
               "TC": range(5729, 5826),
               "TY": range(5826, 5891),
               "CO1": range(5891, 7445),
               "TS1": range(7445, 7514),
               "TD": range(7514, 7585),
               "CO2": range(7585, 8269),
               "TK": range(8269, 8364),
               "ATP8": range(8364, 8572),
               "ATP6": range(8572, 9207),
               "CO3": range(9207, 9990),
               "TG": range(9990, 10058),
               "ND3": range(10058, 10404),
               "TR": range(10404, 10469),
               "ND4L": range(10469, 10766),
               "ND4": range(10766, 12137),
               "TH": range(12137, 12206),
               "TS2": range(12206, 12265),
               "TL2": range(12265, 12336),
               "ND5": range(12336, 14148),
               "ND6": range(14148, 14673),
               "TE": range(14673, 14742),
               "CYTB": range(14742, 15887),
               "TT": range(15887, 15953),
               "TP": range(15953, 16023)}

NONHUMAN_HEADERS = (("Locus", "Gene stable ID",
                     "Locus to which the variant belongs"),
                    ("dbSNP", "Variant name", "dbSNP ID of the variant"),
                    ("Consequence", "Variant consequence",
                     "Functional effect of the variant"))

SPECIES = ("oaries", "ptroglodytes", "scerevisiae", "ecaballus", "fcatus",
           "cfamiliaris", "pabelii", "ggallus", "mmulatta", "rnorvegicus",
           "btaurus", "oanatinus", "sscrofa", "nleucogenys", "chircus",
           "mmusculus", "tguttata", "tnigroviridis", "mgallopavo",
           "mdomestica", "drerio")

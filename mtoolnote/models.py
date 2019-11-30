#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Main(Base):
    __tablename__ = "Main"

    id = Column(Integer, primary_key=True)
    group = Column(String)
    nt_start = Column(Integer)
    ref_rCRS = Column(String)
    alt = Column(String)
    nt_end = Column(Integer)
    locus = Column(String)
    codon_position = Column(Integer)
    aa_change = Column(String)
    disease_score = Column(Float)
    pathogenicity = Column(String)
    haplogroups = Column(String)
    # relationships
    variabId = Column(Integer, ForeignKey("Variab.id"))
    plasmyId = Column(Integer, ForeignKey("Plasmy.id"))
    predictId = Column(Integer, ForeignKey("Predict.id"))
    crossRefId = Column(Integer, ForeignKey("CrossRef.id"))
    # haploFreqsId = Column(Integer, ForeignKey("HaploFreqs.id"))
    # annotId = Column(Integer, ForeignKey("Annot.id"))

    def to_dict(self):
        return {
            "id": self.id, "group": self.group,
            "nt_start": self.nt_start,
            "ref_rCRS": self.ref_rCRS,
            "alt": self.alt,
            "nt_end": self.nt_end,
            "locus": self.locus,
            "codon_position": self.codon_position,
            "aa_change": self.aa_change,
            "disease_score": self.disease_score,
            "pathogenicity": self.pathogenicity,
            "haplogroups": self.haplogroups
        }

    def __repr__(self):
        return """Main(id: {self.id}, group: {self.group}, 
        nt_start: {self.nt_start}, 
        ref_rCRS: {self.ref_rCRS}, alt: {self.alt}, nt_end: {self.nt_end}, 
        locus: {self.locus}, codon_position: {self.codon_position}, 
        aa_change: {self.aa_change}, disease_score: {self.disease_score}, 
        pathogenicity: {self.pathogenicity})\n""".format(self=self)


# class Annot(Base):
#     __tablename__ = "Annot"
#
#     id = Column(Integer, primary_key=True)
#     model_position = Column(Integer)
#     model = Column(String)
#     stem_loop = Column(String)
#     base = Column(String)
#     strutt_3 = Column(String)
#     # relationships
#     mainId = relationship("Main", backref="Annot", lazy="dynamic")
#
#     def to_dict(self):
#         return {
#             "id": self.id, "model_position": self.model_position,
#             "model": self.model, "stem_loop": self.stem_loop, "base": self.base,
#             "strutt_3": self.strutt_3
#         }
#
#     def __repr__(self):
#         return """Annot(id: {self.id}, model_position: {self.model_position},
#         model: {self.model}, stem_loop: {self.stem_loop}, base: {self.base},
#         strutt_3: {self.strutt_3})\n""".format(self=self)


# class HaploFreqs(Base):
#     __tablename__ = "HaploFreqs"
#
#     id = Column(Integer, primary_key=True)
#     group = Column(String)
#     haplo_A = Column(Float)
#     haplo_B = Column(Float)
#     haplo_D = Column(Float)
#     haplo_G = Column(Float)
#     haplo_JT = Column(Float)
#     haplo_L0 = Column(Float)
#     haplo_L1 = Column(Float)
#     haplo_L2 = Column(Float)
#     haplo_L3_star = Column(Float)
#     haplo_L4 = Column(Float)
#     haplo_L5 = Column(Float)
#     haplo_L6 = Column(Float)
#     haplo_M7 = Column(Float)
#     haplo_M8 = Column(Float)
#     haplo_M9 = Column(Float)
#     haplo_M_star = Column(Float)
#     haplo_N1 = Column(Float)
#     haplo_N2 = Column(Float)
#     haplo_N9 = Column(Float)
#     haplo_N_star = Column(Float)
#     haplo_R0 = Column(Float)
#     haplo_R9 = Column(Float)
#     haplo_R_star = Column(Float)
#     haplo_U = Column(Float)
#     haplo_X = Column(Float)
#     # relationships
#     mainId = relationship("Main", backref="HaploFreqs", lazy="dynamic")
#
#     def to_dict(self):
#         return {
#             "id": self.id, "group": self.group,
#             "haplo_A": self.haplo_A, "haplo_B": self.haplo_B,
#             "haplo_D": self.haplo_D, "haplo_G": self.haplo_G,
#             "haplo_JT": self.haplo_JT, "haplo_L0": self.haplo_L0,
#             "haplo_L1": self.haplo_L1, "haplo_L2": self.haplo_L2,
#             "haplo_L3_star": self.haplo_L3_star, "haplo_L4": self.haplo_L4,
#             "haplo_L5": self.haplo_L5, "haplo_L6": self.haplo_L6,
#             "haplo_M7": self.haplo_M7, "haplo_M8": self.haplo_M8,
#             "haplo_M9": self.haplo_M9, "haplo_M_star": self.haplo_M_star,
#             "haplo_N1": self.haplo_N1, "haplo_N2": self.haplo_N2,
#             "haplo_N9": self.haplo_N9, "haplo_N_star": self.haplo_N_star,
#             "haplo_R0": self.haplo_R0, "haplo_R9": self.haplo_R9,
#             "haplo_R_star": self.haplo_R_star, "haplo_U": self.haplo_U,
#             "haplo_X": self.haplo_X
#         }
#
#     def __repr__(self):
#         return """HaploFreqs(id: {self.id}, group: {self.group},
#         haplo_A: {self.haplo_A}, haplo_B: {self.haplo_B},
#         haplo_D: {self.haplo_D}, haplo_G: {self.haplo_G},
#         haplo_JT: {self.haplo_JT}, haplo_L0: {self.haplo_L0},
#         haplo_L1: {self.haplo_L1}, haplo_L2: {self.haplo_L2},
#         haplo_L3_star: {self.haplo_L3_star}, haplo_L4: {self.haplo_L4},
#         haplo_L5: {self.haplo_L5}, haplo_L6: {self.haplo_L6},
#         haplo_M7: {self.haplo_M7}, haplo_M8: {self.haplo_M8},
#         haplo_M9: {self.haplo_M9}, haplo_M_star: {self.haplo_M_star},
#         haplo_N1: {self.haplo_N1}, haplo_N2: {self.haplo_N2},
#         haplo_N9: {self.haplo_N9}, haplo_N_star: {self.haplo_N_star},
#         haplo_R0: {self.haplo_R0}, haplo_R9: {self.haplo_R9},
#         haplo_R_star: {self.haplo_R_star}, haplo_U: {self.haplo_U},
#         haplo_X: {self.haplo_X})\n""".format(self=self)


class Variab(Base):
    __tablename__ = "Variab"

    id = Column(Integer, primary_key=True)
    group = Column(String)
    nt_var = Column(Float)
    nt_var_patients = Column(Float)
    aa_var = Column(Float)
    aa_var_patients = Column(Float)
    all_freq_h = Column(Float)
    all_freq_h_AF = Column(Float)
    all_freq_h_AM = Column(Float)
    all_freq_h_AS = Column(Float)
    all_freq_h_EU = Column(Float)
    all_freq_h_OC = Column(Float)
    all_freq_p = Column(Float)
    all_freq_p_AF = Column(Float)
    all_freq_p_AM = Column(Float)
    all_freq_p_AS = Column(Float)
    all_freq_p_EU = Column(Float)
    all_freq_p_OC = Column(Float)
    # relationships
    mainId = relationship("Main", backref="Variab", lazy="dynamic")

    def to_dict(self):
        return {
            "id": self.id, "group": self.group,
            "nt_var": self.nt_var,
            "nt_var_patients": self.nt_var_patients,
            "aa_var": self.aa_var,
            "aa_var_patients": self.aa_var_patients,
            # "all_freq_h": self.all_freq_h,
            # "all_freq_h_AF": self.all_freq_h_AF,
            # "all_freq_h_AM": self.all_freq_h_AM,
            # "all_freq_h_AS": self.all_freq_h_AS,
            # "all_freq_h_EU": self.all_freq_h_EU,
            # "all_freq_h_OC": self.all_freq_h_OC,
            # "all_freq_p": self.all_freq_p,
            # "all_freq_p_AF": self.all_freq_p_AF,
            # "all_freq_p_AM": self.all_freq_p_AM,
            # "all_freq_p_AS": self.all_freq_p_AS,
            # "all_freq_p_EU": self.all_freq_p_EU,
            # "all_freq_p_OC": self.all_freq_p_OC
        }

    def __repr__(self):
        return """Variab(id: {self.id}, group: {self.group}, nt_var: {self.nt_var}, 
        nt_var_patients: {self.nt_var_patients}, aa_var: {self.aa_var}, 
        aa_var_patients: {self.aa_var_patients}, all_freq_h: {self.all_freq_h}, 
        all_freq_h_AF: {self.all_freq_h_AF}, all_freq_h_AM: {self.all_freq_h_AM}, 
        all_freq_h_AS: {self.all_freq_h_AS}, all_freq_h_EU: {self.all_freq_h_EU}, 
        all_freq_h_OC: {self.all_freq_h_OC}, all_freq_p: {self.all_freq_p}, 
        all_freq_p_AF: {self.all_freq_p_AF}, all_freq_p_AM: {self.all_freq_p_AM}, 
        all_freq_p_AS: {self.all_freq_p_AS}, all_freq_p_EU: {self.all_freq_p_EU}, 
        all_freq_p_OC: {self.all_freq_p_OC})\n""".format(self=self)


class Plasmy(Base):
    __tablename__ = "Plasmy"

    id = Column(Integer, primary_key=True)
    group = Column(String)
    mitomap_homo = Column(String)
    mitomap_hetero = Column(String)
    sm_homo = Column(String)
    sm_hetero = Column(String)
    genomes1K_homo = Column(String)
    genomes1K_hetero = Column(String)
    # relationships
    mainId = relationship("Main", backref="Plasmy", lazy="dynamic")

    def to_dict(self):
        return {
            # "id": self.id, "group": self.group,
            "mitomap_homo": self.mitomap_homo,
            "mitomap_hetero": self.mitomap_hetero, "sm_homo": self.sm_homo,
            "sm_hetero": self.sm_hetero, "genomes1K_homo": self.genomes1K_homo,
            "genomes1K_hetero": self.genomes1K_hetero
        }

    def __repr__(self):
        return """Plasmy(id: {self.id}, group: {self.group}, 
        mitomap_homo: {self.mitomap_homo}, mitomap_hetero: {self.mitomap_hetero}, 
        sm_homo: {self.sm_homo}, sm_hetero: {self.sm_hetero}, 
        genomes1K_homo: {self.genomes1K_homo}, 
        genomes1K_hetero: {self.genomes1K_hetero})\n""".format(self=self)


class Predict(Base):
    __tablename__ = "Predict"

    id = Column(Integer, primary_key=True)
    group = Column(String)
    mutPred_pred = Column(String)
    mutPred_prob = Column(Float)
    polyphen2_humDiv_pred = Column(String)
    polyphen2_humDiv_prob = Column(Float)
    polyphen2_humVar_pred = Column(String)
    polyphen2_humVar_prob = Column(Float)
    panther_pred = Column(String)
    panther_prob = Column(Float)
    phD_snp_pred = Column(String)
    phD_snp_prob = Column(Float)
    snp_go_pred = Column(String)
    snp_go_prob = Column(Float)
    clinvar_pred = Column(String)
    clinvar_pheno = Column(String)
    # relationships
    mainId = relationship("Main", backref="Predict", lazy="dynamic")

    def to_dict(self):
        return {
            # "id": self.id, "group": self.group,
            "mutPred_pred": self.mutPred_pred,
            "mutPred_prob": self.mutPred_prob,
            "polyphen2_humDiv_pred": self.polyphen2_humDiv_pred,
            "polyphen2_humDiv_prob": self.polyphen2_humDiv_prob,
            "polyphen2_humVar_pred": self.polyphen2_humVar_pred,
            "polyphen2_humVar_prob": self.polyphen2_humVar_prob,
            "panther_pred": self.panther_pred,
            "panther_prob": self.panther_prob,
            "phD_snp_pred": self.phD_snp_pred,
            "phD_snp_prob": self.phD_snp_prob,
            "snp_go_pred": self.snp_go_pred,
            "snp_go_prob": self.snp_go_prob,
            # "clinvar_pred": self.clinvar_pred,
            # "clinvar_pheno": self.clinvar_pheno
        }

    def __repr__(self):
        return """Predict(id: {self.id}, group: {self.group}, 
        mutPred_pred: {self.mutPred_pred}, 
        mutPred_prob: {self.mutPred_prob}, 
        polyphen2_humDiv_pred: {self.polyphen2_humDiv_pred}, 
        polyphen2_humDiv_prob: {self.polyphen2_humDiv_prob}, 
        polyphen2_humVar_pred: {self.polyphen2_humVar_pred}, 
        polyphen2_humVar_prob: {self.polyphen2_humVar_prob}, 
        panther_pred: {self.panther_pred}, 
        panther_prob: {self.panther_prob}, phD_snp_pred: {self.phD_snp_pred}, 
        phD_snp_prob: {self.phD_snp_prob}, snp_go_pred: {self.snp_go_pred}, 
        snp_go_prob: {self.snp_go_prob}, clinvar_pred: {self.clinvar_pred}, 
        clinvar_pheno: {self.clinvar_pheno})\n""".format(self=self)


class CrossRef(Base):
    __tablename__ = "CrossRef"

    id = Column(Integer, primary_key=True)
    group = Column(String)
    clinvar = Column(String)
    omim = Column(String)
    dbSNP = Column(String)
    mamit_tRNA = Column(String)
    phastCons_100way = Column(Float)
    phyloP_100way = Column(Float)
    ac_an_genomes1K = Column(Float)
    mitomap_associated_disease = Column(String)
    somatic_mutations = Column(String)
    pubs_disease = Column(String)
    # relationships
    mainId = relationship("Main", backref="CrossRef", lazy="dynamic")

    def to_dict(self):
        return {
            # "id": self.id, "group": self.group,
            "clinvar": self.clinvar,
            "omim": self.omim,
            "dbSNP": self.dbSNP,
            # "mamit_tRNA": self.mamit_tRNA,
            # "phastCons_100way": self.phastCons_100way,
            # "phyloP_100way": self.phyloP_100way,
            # "ac_an_genomes1K": self.ac_an_genomes1K,
            # "mitomap_associated_disease": self.mitomap_associated_disease,
            # "somatic_mutations": self.somatic_mutations,
            # "pubs_disease": self.pubs_disease
        }

    def __repr__(self):
        return """CrossRef(id: {self.id}, group: {self.group}, 
        clinvar: {self.clinvar}, 
        omim: {self.omim}, dbSNP: {self.dbSNP}, mamit_tRNA: {self.mamit_tRNA}, 
        phastCons_100way: {self.phastCons_100way}, 
        phyloP_100way: {self.phyloP_100way}, 
        ac_an_genomes1K: {self.ac_an_genomes1K}, 
        mitomap_associated_disease: {self.mitomap_associated_disease}, 
        somatic_mutations: {self.somatic_mutations}, 
        pubs_disease: {self.pubs_disease})\n""".format(self=self)


class Func_Loci(Base):
    __tablename__ = "FuncLoci"

    id = Column(Integer, primary_key=True)
    locus = Column(String)
    nt_start = Column(Integer)
    nt_end = Column(Integer)
    description = Column(String)

    def to_dict(self):
        return {
            "id": self.id, "locus": self.locus, "nt_start": self.nt_start,
            "nt_end": self.nt_end, "description": self.description
        }

    def __repr__(self):
        return """Func_Loci(id: {self.id}, locus: {self.locus}, 
        nt_start: {self.nt_start}, nt_end: {self.nt_end}, 
        description: {self.description})\n""".format(self=self)


class Loci(Base):
    __tablename__ = "Loci"

    id = Column(Integer, primary_key=True)
    group = Column(String)
    locus = Column(String)
    nt_start = Column(Integer)
    nt_end = Column(Integer)
    description = Column(String)
    length = Column(Integer)
    dna_seq = Column(String)
    aa_seq = Column(String)

    def to_dict(self):
        return {
            "id": self.id, "group": self.group, "locus": self.locus,
            "nt_start": self.nt_start, "nt_end": self.nt_end,
            "description": self.description, "length": self.length,
            "dna_seq": self.dna_seq, "aa_seq": self.aa_seq
        }

    def __repr__(self):
        return """Loci(id: {self.id}, group: {self.group}, locus: {self.locus}, 
        nt_start: {self.nt_start}, nt_end: {self.nt_end}, 
        description: {self.description}, length: {self.length}, 
        dna_seq: {self.dna_seq}, aa_seq: {self.aa_seq})\n""".format(self=self)


class Haplo_A(Base):
    __tablename__ = "Haplo_A"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C,
                "freq_G": self.freq_G, "freq_T": self.freq_T,
                "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_A(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_B(Base):
    __tablename__ = "Haplo_B"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_B(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_D(Base):
    __tablename__ = "Haplo_D"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_D(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_G(Base):
    __tablename__ = "Haplo_G"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_G(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_JT(Base):
    __tablename__ = "Haplo_JT"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_JT(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_L0(Base):
    __tablename__ = "Haplo_L0"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_L0(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_L1(Base):
    __tablename__ = "Haplo_L1"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_L1(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_L2(Base):
    __tablename__ = "Haplo_L2"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_L2(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_L3_star(Base):
    __tablename__ = "Haplo_L3_star"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_L3_star(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_L4(Base):
    __tablename__ = "Haplo_L4"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_L4(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_L5(Base):
    __tablename__ = "Haplo_L5"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_L5(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_L6(Base):
    __tablename__ = "Haplo_L6"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_L6(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_M7(Base):
    __tablename__ = "Haplo_M7"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_M7(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_M8(Base):
    __tablename__ = "Haplo_M8"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_M8(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_M9(Base):
    __tablename__ = "Haplo_M9"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_M9(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_M_star(Base):
    __tablename__ = "Haplo_M_star"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_M_star(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_N1(Base):
    __tablename__ = "Haplo_N1"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_N1(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_N2(Base):
    __tablename__ = "Haplo_N2"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_N2(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_N9(Base):
    __tablename__ = "Haplo_N9"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_N9(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_N_star(Base):
    __tablename__ = "Haplo_N_star"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_N_star(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_R0(Base):
    __tablename__ = "Haplo_R0"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_R0(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_R9(Base):
    __tablename__ = "Haplo_R9"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_R9(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_R_star(Base):
    __tablename__ = "Haplo_R_star"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_R_star(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_U(Base):
    __tablename__ = "Haplo_U"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_U(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)


class Haplo_X(Base):
    __tablename__ = "Haplo_X"

    id = Column(Integer, primary_key=True)
    position = Column(String, primary_key=True)
    freq_A = Column(Float)
    freq_C = Column(Float)
    freq_G = Column(Float)
    freq_T = Column(Float)
    freq_gap = Column(Float)
    freq_oth = Column(Float)

    def to_dict(self):
        return {"position": self.position, "freq_A": self.freq_A, "freq_C": self.freq_C, "freq_G": self.freq_G,
                "freq_T": self.freq_T, "freq_gap": self.freq_gap, "freq_oth": self.freq_oth}

    def __repr__(self):
        return """Haplo_X(id: {self.id}, position: {self.position}, freq_A: {self.freq_A}, 
        freq_C: {self.freq_C}, freq_G: {self.freq_G}, freq_T: {self.freq_T}, 
        freq_gap: {self.freq_gap}, freq_oth: {self.freq_oth})\n""".format(self=self)

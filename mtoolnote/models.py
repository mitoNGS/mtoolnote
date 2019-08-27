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
    # annotId = Column(Integer, ForeignKey("Annot.id"))

    def to_dict(self):
        return {
            "id": self.id, "group": self.group, "nt_start": self.nt_start,
            "ref_rCRS": self.ref_rCRS, "alt": self.alt, "nt_end": self.nt_end,
            "locus": self.locus, "codon_position": self.codon_position,
            "aa_change": self.aa_change, "disease_score": self.disease_score,
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
            "id": self.id, "group": self.group, "nt_var": self.nt_var,
            "nt_var_patients": self.nt_var_patients, "aa_var": self.aa_var,
            "aa_var_patients": self.aa_var_patients,
            "all_freq_h": self.all_freq_h,
            "all_freq_h_AF": self.all_freq_h_AF,
            "all_freq_h_AM": self.all_freq_h_AM,
            "all_freq_h_AS": self.all_freq_h_AS,
            "all_freq_h_EU": self.all_freq_h_EU,
            "all_freq_h_OC": self.all_freq_h_OC,
            "all_freq_p": self.all_freq_p,
            "all_freq_p_AF": self.all_freq_p_AF,
            "all_freq_p_AM": self.all_freq_p_AM,
            "all_freq_p_AS": self.all_freq_p_AS,
            "all_freq_p_EU": self.all_freq_p_EU,
            "all_freq_p_OC": self.all_freq_p_OC
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
            "id": self.id, "group": self.group,
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
            "id": self.id, "group": self.group,
            "mutPred_pred": self.mutPred_pred,
            "mutPred_prob": self.mutPred_prob,
            "polyphen2_humDiv_pred": self.polyphen2_humDiv_pred,
            "polyphen2_humDiv_prob": self.polyphen2_humDiv_prob,
            "polyphen2_humVar_pred": self.polyphen2_humVar_pred,
            "polyphen2_humVar_prob": self.polyphen2_humVar_prob,
            "panther_pred": self.panther_pred,
            "panther_prob": self.panther_prob,
            "phD_snp_pred": self.phD_snp_pred, "phD_snp_prob": self.phD_snp_prob,
            "snp_go_pred": self.snp_go_pred, "snp_go_prob": self.snp_go_prob,
            "clinvar_pred": self.clinvar_pred,
            "clinvar_pheno": self.clinvar_pheno
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
            "id": self.id, "group": self.group, "clinvar": self.clinvar,
            "omim": self.omim, "dbSNP": self.dbSNP,
            "mamit_tRNA": self.mamit_tRNA,
            "phastCons_100way": self.phastCons_100way,
            "phyloP_100way": self.phyloP_100way,
            "ac_an_genomes1K": self.ac_an_genomes1K,
            "mitomap_associated_disease": self.mitomap_associated_disease,
            "somatic_mutations": self.somatic_mutations,
            "pubs_disease": self.pubs_disease
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

=====
Usage
=====

Once installed, mtoolnote offers a CLI command and a Python function to annotate both human and non-human VCF files.

Human mitochondrial variant annotation
--------------------------------------

Using the CLI::

    $ mtoolnote INPUT_VCF OUTPUT_VCF

where ``INPUT_VCF`` and ``OUTPUT_VCF`` represent file paths.

Using the Python module::

    import mtoolnote
    mtoolnote.annotate("input.vcf", "output.vcf")

Non-human mitochondrial variant annotation
------------------------------------------

Using the CLI::

    $ mtoolnote INPUT_VCF OUTPUT_VCF SPECIES

where SPECIES indicates the sample species, one of ``oaries``, ``ptroglodytes``, ``scerevisiae``,
``ecaballus``, ``fcatus``, ``cfamiliaris``, ``pabelii``, ``ggallus``, ``mmulatta``,
``rnorvegicus``, ``btaurus``, ``oanatinus``, ``sscrofa``, ``nleucogenys``, ``chircus``,
``mmusculus``, ``tguttata``, ``tnigroviridis``, ``mgallopavo``, ``mdomestica``, ``drerio``.

Using the Python module::

    import mtoolnote
    mtoolnote.annotate("input.vcf", "output_vcf", "species")

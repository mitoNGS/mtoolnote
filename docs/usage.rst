=====
Usage
=====

Once installed, mtoolnote offers a CLI command and a Python function to annotate both human and non-human VCF files.

Human mitochondrial variant annotation
--------------------------------------

Using the CLI::

    $ mtoolnote INPUT_VCF OUTPUT_VCF

where ``INPUT_VCF`` and ``OUTPUT_VCF`` represent file paths. Use the ``--csv`` flag option to create an annotated CSV file in addition to the VCF output.

Using the Python module::

    import mtoolnote
    mtoolnote.annotate("input.vcf", "output.vcf")

Use the ``csv=True`` option to create an annotated CSV file in addition to the VCF output.

Non-human mitochondrial variant annotation
------------------------------------------

Using the CLI::

    $ mtoolnote INPUT_VCF OUTPUT_VCF SPECIES

where SPECIES indicates the sample species, one of ``oaries``, ``ptroglodytes``, ``scerevisiae``,
``ecaballus``, ``fcatus``, ``cfamiliaris``, ``pabelii``, ``ggallus``, ``mmulatta``,
``rnorvegicus``, ``btaurus``, ``oanatinus``, ``sscrofa``, ``nleucogenys``, ``chircus``,
``mmusculus``, ``tguttata``, ``tnigroviridis``, ``mgallopavo``, ``mdomestica``, ``drerio``. Use the ``--csv`` flag option to create an annotated CSV file in addition to the VCF output.

Using the Python module::

    import mtoolnote
    mtoolnote.annotate("input.vcf", "output_vcf", "species")

Use the ``csv=True`` option to create an annotated CSV file in addition to the VCF output.

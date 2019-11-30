=========
mtoolnote
=========


.. image:: https://www.repostatus.org/badges/latest/wip.svg
    :alt: Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.
    :target: https://www.repostatus.org/#wip


Variant annotator for MToolBox.


* Free software: MIT license
* GitHub repo: https://github.com/mitoNGS/mtoolnote


Features
========

mtoolnote can annotate mitochondrial variants from:

* human genomes, using data stored in a local database derived from HmtVar_;
* non-human genomes, using data from BioMart_.
    - Currently, only the following species are supported: oaries, ptroglodytes, scerevisiae
        ecaballus, fcatus, cfamiliaris, pabelii, ggallus, mmulatta, rnorvegicus, btaurus,
        oanatinus, sscrofa, nleucogenys, chircus, mmusculus, tguttata, tnigroviridis,
        mgallopavo, mdomestica, drerio

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

Installation
============

After cloning this repo, ``cd`` in it and install mtoolnote using::

    $ python setup.py install
    # in case this does not work:
    $ pip install -r requirements.txt
    $ pip install .

or in development mode::

    $ pip install -r requirements_dev.txt
    $ pip install -e .

Testing
-------

After installation, run all tests with::

    $ pytest

or the full suite (tests using python3.6, python3.7, flake8) with::

    $ tox

Credits
=======

This package was created with Cookiecutter_ and the `cc-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cc-pypackage`: https://github.com/robertopreste/cc-pypackage
.. _Usage: https://mtoolnote.readthedocs.io/en/latest/usage.html
.. _Installation: https://mtoolnote.readthedocs.io/en/latest/installation.html
.. _HmtVar: https://www.hmtvar.uniba.it
.. _BioMart: https://www.ensembl.org/biomart/martview

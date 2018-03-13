===============
Odoo Lci-odoo10
===============

.. contents::

Development environment howto
=============================

Initialize virtualenv
---------------------

create and activate virtualenv, possibly with virtualenvwrapper's
``mkvirtualenv odoo-lci-odoo10 -a .``

To save some time copy Odoo 10.0 sources in src/odoo,
and do ``git clean -ffdx`` in src/odoo.

Install everything
------------------

.. code:: bash

   pip install --src src -r requirements.txt -e .

Only when there is a need to refresh the frozen dependencies,
review ``gitaggregate.yaml`` and ``requirements-dev.txt``, then
run:

.. code:: bash

   gitaggregate -c gitaggregate.yaml -p
   rmvirtualenv odoo-lci-odoo10
   mkvirtualenv odoo-lci-odoo10 -a .
   pip install --src src --pre -r requirements-dev.txt
   ./freeze.sh
   git commit requirements.txt

Run
---

   odoo

Release
-------

First make sure you have been testing using the correct dependencies by
running ``./freeze.sh`` and checking there is no change in ``requirements.txt``.

To relase using gitlab-ci
.........................

- run acsoo tag, the deploy to the test environment will be automatic, and
  gitlab will show a button on the pipeline to deploy to production.

To release manually
...................

- update version in ``acsoo.cfg`` and ``lci-odoo10_all/__manifest__.py``
- commit everything
- run ``acsoo release``

At that point the resulting wheel files in ``./release`` contain all the
code to be deployed.

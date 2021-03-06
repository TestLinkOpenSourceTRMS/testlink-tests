Testlink-tests
==============


.. image:: https://img.shields.io/github/issues/TestLinkOpenSourceTRMS/testlink-tests.svg
  :alt: Issues on Github
  :target: https://github.com/TestLinkOpenSourceTRMS/testlink-tests/issues

.. image:: https://img.shields.io/github/issues-pr/TestLinkOpenSourceTRMS/testlink-tests.svg
  :alt: Pull Request opened on Github
  :target: https://github.com/TestLinkOpenSourceTRMS/testlink-tests/issues

.. image:: https://img.shields.io/github/release/TestLinkOpenSourceTRMS/testlink-tests.svg
  :alt: Release version on Github
  :target: https://github.com/TestLinkOpenSourceTRMS/testlink-tests/releases/latest

.. image:: https://img.shields.io/github/release-date/TestLinkOpenSourceTRMS/testlink-tests.svg
  :alt: Release date on Github
  :target: https://github.com/TestLinkOpenSourceTRMS/testlink-tests/releases/latest


+-----------------------+-----------------------+--------------------------+--------------------------+------------------------------+
| Branch                |     TravisCI          |     Appveyor             |   CircleCi - Docker      |   CodeClimate                |
+=======================+=======================+==========================+==========================+==============================+
|  master               |  |master_ci_travis|   |   |master_ci_appveyor|   |   |master_ci_circleci|   |   |master_ci_codeclimate|    |
+-----------------------+-----------------------+--------------------------+--------------------------+------------------------------+


Python tested versions
----------------------

+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+
|  **3.6**          |  **3.5**          |  **3.4**          |  **3.3**          |  **3.2**          |  **2.7**          |
+===================+===================+===================+===================+===================+===================+
|    *Supported*    |    *Supported*    |    *Supported*    |  *Not Supported*  |  *Not Supported*  |    *Supported*    |
+-------------------+-------------------+-------------------+-------------------+-------------------+-------------------+


Prerequisites
-------------

+ Need Testlink WebApp **Up and Running**


How to install ?
----------------

+ Install from PIP : ``pip install testlinktests``

+ Install from setup.py file : ``python setup.py install``



How to exec tests ?
-------------------

+ Tests from setup.py file : ``python setup.py test``

+ Install from PIP file : ``pip install tox``
+ Tests from tox : ``tox -l && tox -e TOX_ENV_NAME`` ( *see tox.ini file to get environment names* )


+---------------------+--------------------------------+
| TOX Env name        | Env description                |
+=====================+================================+
| py27,py34,py35,py36 | Python supported versions      |
+---------------------+--------------------------------+
| flake8              | Exec linter in qalab/ tests/   |
+---------------------+--------------------------------+
| coverage            | Generate XML and HTML reports  |
+---------------------+--------------------------------+

Configuration File
~~~~~~~~~~~~~~~~~~


::

    {
      "connection":{
        "is_https": false,
        "host": "qalab.tk",
        "port": 86
      },
      "dev_key": "1bfd2ef4ceda22b482b12f2b25457495",
      "log_level":"DEBUG",
    }

Getting Started
~~~~~~~~~~~~~~~

*Just starting example of usage before read* `Usage Guide`_.


.. _Usage Guide: USAGE.rst
.. |master_ci_travis| image:: https://travis-ci.com/TestLinkOpenSourceTRMS/testlink-tests.svg?branch=master
  :target: https://travis-ci.com/TestLinkOpenSourceTRMS/testlink-tests
.. |master_ci_appveyor| image:: https://ci.appveyor.com/api/projects/status/5rcuh1wj3rissqu64wmb/branch/master?svg=true
  :target: https://ci.appveyor.com/project/netzulo/testlink-tests
.. |master_ci_circleci| image:: https://circleci.com/gh/TestLinkOpenSourceTRMS/testlink-tests.svg?style=svg
  :target: https://circleci.com/gh/netzulo/testlink-tests)
.. |master_ci_codeclimate| image:: https://api.codeclimate.com/v1/badges/-/maintainability
  :target: https://codeclimate.com/github/TestLinkOpenSourceTRMS/testlink-tests/maintainability

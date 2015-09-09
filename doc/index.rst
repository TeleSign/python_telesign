###########################################
TeleSign Python SDK |version| Documentation
###########################################

********
Overview
********

**TeleSign Web Services** conform to the `REST Web Service Design Model <http://en.wikipedia.org/wiki/Representational_state_transfer>`_. Services are exposed as URI-addressable resources through the set of *RESTful* procedures in our **TeleSign REST API**.

The **TeleSign Python SDK** is a set of software development tools; a *Python Library* that wraps the TeleSign REST API, and it simplifies TeleSign application development in the `Python programming language <http://www.python.org/>`_. The SDK software is listed in the `Python Package Index (PyPI) <http://pypi.python.org>`_, as the **telesign** Python package.

:doc:`installation`
  Instructions on how to get the package.

:doc:`api/telesign.api`
  The complete API documentation, organized by module.

:doc:`api/telesign.exceptions`
    Exception classes for error handling.

  
************
Getting Help
************

If you're having trouble, or have questions about TeleSign, please contact our customer support team:

Email: `support@telesign.com <mailto:support@telesign.com>`_


************************
About This Documentation
************************

This documentation contains information on how to download and install the **TeleSign Python SDK**, and it contains a comprehensive set of Python language reference pages that detail the TeleSign Python classes and methods that wrap the TeleSign REST API.

This documentation was generated using the `Sphinx <http://sphinx.pocoo.org/>`_ documentation generator. The source files for the documentation are located in the *doc/* directory of the **telesign** distribution. You can regenerate the docs locally by running the following command from the root directory of the **telesign** source:

.. code-block:: bash

  $ python setup.py doc


*****************
Documentation Map
*****************

.. toctree::
    :maxdepth: -1
    
    installation
    api/index
    api/telesign.api
    api/telesign.exceptions

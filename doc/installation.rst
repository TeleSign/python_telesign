.. highlight:: bash

***************
:mod:`telesign`
***************

The **telesign** Python Package contains the **TeleSign Python SDK** software, and it is registered with the `Python Package Index (PyPI) <http://pypi.python.org/pypi/telesign/>`_.


:obj:`Installing the SDK`
=========================

There are three approaches you can use to install the SDK:


Using *pip*
^^^^^^^^^^^^^

    On platforms other than Windows, we recommend using `pip <http://pypi.python.org/pypi/pip>`_ to install **telesign**, using the following command::
    
        $ pip install telesign
    
    To install a specific version of **telesign**, simply add the version number to the command line, as in the following example::
    
        $ pip install telesign==1.0.0
    
    To upgrade an existing telesign installation, use the *--upgrade* switch, as in the following example::
    
        $ pip install --upgrade telesign


Using *easy_install*
^^^^^^^^^^^^^^^^^^^^^^

    On Windows-based Python deployments, you can use `Easy Install <http://packages.python.org/distribute/easy_install.html>`_
    to install **telesign**, using the following command::
    
        $ easy_install telesign
    
    To upgrade an existing telesign installation, use the *-U* switch, as in the following example::
    
        $ easy_install -U telesign


Using our *source*
^^^^^^^^^^^^^^^^^^^^

    If you would like to try-out the *latest* bits, you can clone a local version of our public source code repository on `GitHub <https://github.com/telesign>`_, and then install from your enlistment, as in the following example::
    
        $ git clone git://github.com/TeleSign/python_telesign.git telesign
        $ cd telesign/
        $ python setup.py install

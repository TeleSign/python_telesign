:mod:`telesign.api`
===================
The **telesign.api** module contains Python classes and methods that allow you to use the Python programming language to programmatically access the **Verify** and the **PhoneId** TeleSign web services, and the TeleSign **Account** key management service.

.. currentmodule:: telesign.api

.. autosummary::
    :toctree: generated
    :nosignatures:

    Verify
    PhoneId
    Account


:mod:`telesign.api.Verify`
--------------------------

.. currentmodule:: telesign.api.Verify

.. autosummary::
    :nosignatures:
    
    call
    sms
    status


:mod:`telesign.api.PhoneId`
---------------------------

.. currentmodule:: telesign.api.PhoneId

.. autosummary::
    :nosignatures:

    standard
    score
    contact
    live


:mod:`telesign.exceptions`
==========================

You need the telesign.exceptions module to handle the exception conditions raised by the functions in the **telesign.api** module.

.. currentmodule:: telesign.exceptions

.. autosummary::
    :toctree: generated
    :nosignatures:
    
    TelesignError
    AuthorizationError
    ValidationError

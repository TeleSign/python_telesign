"""

.. :module:: telesign.exceptions
    :synopsis: The **exceptions** module contains exception classes for handling the error conditions that can be thrown by procedures in the **api** module.

"""

__author__ = "Jeremy Cunningham, Michael Fox, and Radu Maierean"
__copyright__ = "Copyright 2015, TeleSign Corp."
__credits__ = ["Jeremy Cunningham", "Radu Maierean", "Michael Fox", "Nancy Vitug", "Humberto Morales"]
__license__ = "MIT"
__maintainer__ = "Jeremy Cunningham"
__email__ = "support@telesign.com"
__status__ = "Production"


class TelesignError(Exception):
    """
    The **exceptions** base class.

    .. list-table::
       :widths: 5 30
       :header-rows: 1

       * - Attributes
         -
       * - `data`
         - The data returned by the service, in a dictionary form.
       * - `http_response`
         - The full HTTP Response object, including the HTTP status code, headers, and raw returned data.

    """

    def __init__(self, data, http_response):
        self.errors = data["errors"]
        self.headers = http_response.headers
        self.status = http_response.status_code
        self.data = data
        self.raw = http_response.raw

    def __str__(self):
        result = ""
        for x in range(0, len(self.errors)):
            result += "%s\n" % self.errors[x]["description"]

        return result


class AuthorizationError(TelesignError):
    """
    Either the client failed to authenticate with the REST API server, or the service cannot be executed using the specified credentials.

    .. list-table::
       :widths: 5 30
       :header-rows: 1

       * - Attributes
         -
       * - `data`
         - The data returned by the service, in a dictionary form.
       * - `http_response`
         - The full HTTP Response object, including the HTTP status code, headers, and raw returned data.

    """

    def __init__(self, data, http_response):
        TelesignError.__init__(self, data, http_response)


class ValidationError(TelesignError):
    """
    The submitted data failed the intial validation, and the service was not executed.

    .. list-table::
       :widths: 5 30
       :header-rows: 1

       * - Attributes
         -
       * - `data`
         - The data returned by the service, in a dictionary form.
       * - `http_response`
         - The full HTTP Response object, including the HTTP status code, headers, and raw returned data.

    """

    def __init__(self, data, http_response):
        TelesignError.__init__(self, data, http_response)

class TokenExpired():
    pass


class APIError(Exception):
    """Raised when sending a request to the API failed."""

    def __init__(self, response):
        super(APIError, self).__init__(response)
        self.response = response


class ValidationError(APIError):
    """Raised when the API returns validation errors."""

    def __init__(self, response):
        super(ValidationError, self).__init__(response)

        data = response.json()
        self.errors = data.get('errors', [])
        self.field_errors = data.get('field-errors', {})

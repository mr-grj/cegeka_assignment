class CSVServiceError(Exception):
    """
    Base exception class for the CV Service.

    This exception is used as the parent class for all exceptions
    related to the CV Service. It provides a common interface and
    can be used to catch all CV Service-specific exceptions.
    """

    ...


class CVFileNotFoundError(CSVServiceError):
    """
    Raised when the provided file path does not exist.
    """

    def __init__(self, filename):
        super().__init__(f"File not found: {filename}.")
        self.filename = filename


class CVInvalidJSONError(CSVServiceError):
    """
    Raised when an invalid JSON data is encountered.
    """

    def __init__(self, filename, original_exception):
        super().__init__(
            f"Invalid JSON data in {filename}. Error: {str(original_exception)}"
        )
        self.filename = filename
        self.original_exception = original_exception

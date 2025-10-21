class AWSHealthCheckError(Exception):
    """Custom exception for AWS health check errors."""
    def __init__(self, message: str):
        super().__init__(message)
    pass


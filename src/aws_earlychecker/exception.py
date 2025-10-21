import typer
class InvalidCommandError(Exception):
    """Base exception for invalid CLI commands."""
    pass


class AWSHealthCheckError(Exception):
    """Custom exception for AWS health check errors."""
    pass


class EmptyCommandError(InvalidCommandError):
    """Raised when no CLI command is entered."""
    def __init__(self):
        super().__init__("No command entered. Please provide a valid command. Use --help for a list of available commands.")


class NoSuchCommandError(InvalidCommandError):
    """Raised when a non-existent command is entered."""
    def __init__(self, command: str):
        super().__init__(f"The command '{command}' does not exist. Use --help for a list of available commands.")


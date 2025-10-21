import typer
from abc import ABC, abstractmethod
class ExceptionHandler(ABC):
    """Interface for defining custom exception handlers."""
    @abstractmethod
    def register_exceptions(app: typer.Typer):
        pass

class DefaultExceptionHandler(ExceptionHandler):
    """Default implementation of ExceptionHandler."""
    def register_exceptions(app: typer.Typer):
        """Register exception handlers for the given errors."""
        from aws_earlychecker.exception import AWSHealthCheckError, EmptyCommandError, InvalidCommandError, NoSuchCommandError
        from click.exceptions import NoSuchOption

        @app.exception_handler(NoSuchOption)
        def handle_no_such_option(exc: NoSuchOption):
            raise NoSuchCommandError(exc.option_name)

        @app.exception_handler(EmptyCommandError)
        def handle_empty_command(exc: EmptyCommandError):
            print(f"[red]❌ {exc}[/red]")
            raise typer.Exit(code=2)

        @app.exception_handler(NoSuchCommandError)
        def handle_no_such_command(exc: NoSuchCommandError):
            print(f"[red]❌ {exc}[/red]")
            raise typer.Exit(code=2)

        @app.exception_handler(AWSHealthCheckError)
        def handle_aws_health_check_error(exc: AWSHealthCheckError):
            print(f"[red]⚠️ AWS Health Check Failed:[/red] {exc}")
            raise typer.Exit(code=3)

        @app.exception_handler(InvalidCommandError)
        def handle_invalid_command_error(exc: InvalidCommandError):
            print(f"[red]❌ Invalid Command:[/red] {exc}")
            raise typer.Exit(code=2)

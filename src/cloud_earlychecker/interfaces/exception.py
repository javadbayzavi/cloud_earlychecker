import typer
from abc import ABC, abstractmethod
from rich import print
from cloud_earlychecker.exceptions.exception import (
    AWSHealthCheckError
)

class ExceptionHandler(ABC):
    """Interface for defining custom exception handlers."""

    @abstractmethod
    def register_exceptions(self, app: typer.Typer):
        pass


class DefaultExceptionHandler(ExceptionHandler):
    """Centralized exception handler for Typer CLI."""

    def register_exceptions(self, app: typer.Typer):
        # You can still store app reference if needed later
        self.app = app
        
        @app.exception_handler(AWSHealthCheckError)
        def handle_aws_health(exc: AWSHealthCheckError):
            print(f"[red]⚠️ AWS Health Check Failed:[/red] {exc}")
            raise typer.Exit(code=3)
        
        @app.exception_handler(Exception)
        def handle_generic_exception(exc: Exception):
            print(f"[red]⚠️ An unexpected error occurred:[/red] {exc}")
            raise typer.Exit(code=1)


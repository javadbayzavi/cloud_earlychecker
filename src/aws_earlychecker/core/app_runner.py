import typer
from typing import Type
from rich import print
from aws_earlychecker.interfaces.cli_interface import CLIInterface
from aws_earlychecker.interfaces.callback import AppCallback

from aws_earlychecker.interfaces.exception import ExceptionHandler

class AppRunner:
    """Responsible for wiring CLI implementations into Typer and executing them."""

    def __init__(self, cli_impl: Type[CLIInterface]):
        self.app = typer.Typer(help="AWS EarlyCheck CLI – detect AWS service degradation early.")
        self.cli_impl = cli_impl

    def setup(self, callback: AppCallback=None, exception_handler=None):
        """Register all commands, callbacks, and error handlers from CLI implementation."""
        cli_instance = self.cli_impl()
        cli_instance.register(self.app, callback=callback)
        return cli_instance
    
    def run(self, callback: AppCallback = None, exception_handler: ExceptionHandler = None):
        """Run the CLI application."""
        instance = self.setup(callback=callback, exception_handler=exception_handler)
        instance.run()
        self.app()

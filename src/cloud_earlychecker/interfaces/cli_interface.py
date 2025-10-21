from abc import ABC, abstractmethod
import typer

from cloud_earlychecker.interfaces.callback import AppCallback
from cloud_earlychecker.interfaces.exception import ExceptionHandler


class CLIInterface(ABC):
    """Interface defining a CLI module that can register commands to a Typer app."""

    @abstractmethod
    def register(self, app: typer.Typer, callback: AppCallback=None, exception_handler: ExceptionHandler=None):
        """Register commands, callbacks, and error handlers to the Typer app."""
        pass

    @abstractmethod
    def run(self):
        """Optional method to perform setup before app runs (e.g., config loading)."""
        pass
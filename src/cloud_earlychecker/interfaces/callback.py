import typer
from abc import ABC, abstractmethod


class AppCallback(ABC):
    @abstractmethod
    def callback(ctx: typer.Context):
        """
        Root callback executed when no subcommand is provided.
        """
        pass
import typer
from abc import ABC, abstractmethod

from cloud_earlychecker.core.app_state import AppState


class AppCallback(ABC):
    @abstractmethod
    def callback(ctx: typer.Context):
        """
        Root callback executed when no subcommand is provided.
        """
        pass
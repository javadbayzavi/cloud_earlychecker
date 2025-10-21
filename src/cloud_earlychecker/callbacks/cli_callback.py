from rich import print
import typer
from cloud_earlychecker.interfaces.callback import AppCallback

class CliCallback(AppCallback):
    """
    Base class for CLI callbacks.
    """

    def callback(self, ctx: typer.Context):
        """
        Root callback executed when no subcommand is provided.
        """
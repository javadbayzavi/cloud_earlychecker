from rich import print
import typer

def version(ctx: typer.Context):
    """
    Display version information.
    """
    if ctx.obj:
        app_state = ctx.obj
        environment = app_state.getEnvironment()
        version_info = environment.get_from_environment("VERSION")
        if version_info:
            print(f"AWS EarlyCheck version from environment: [bold]{version_info}[/bold]")
            return
        else:
            from cloud_earlychecker import __version__
            print(f"AWS EarlyCheck version: [bold]{__version__.__version__}[/bold]")

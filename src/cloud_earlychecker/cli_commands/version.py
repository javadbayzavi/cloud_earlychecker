from rich import print
def version():
    """
    Display version information.
    """
    from cloud_earlychecker import __version__
    print(f"AWS EarlyCheck version: [bold]{__version__.__version__}[/bold]")

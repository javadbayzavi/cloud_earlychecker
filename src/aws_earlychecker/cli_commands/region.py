import typer

def region(region: str = typer.Argument(..., help="AWS region to set as default, e.g., us-east-1")):
    """
    Set default AWS region.
    """
    # Placeholder for setting region logic
    print(f"Default AWS region set to: [bold]{region}[/bold]")

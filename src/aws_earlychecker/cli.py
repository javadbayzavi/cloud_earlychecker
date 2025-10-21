import typer
from aws_earlychecker import core
from rich import print

app = typer.Typer(help="AWS EarlyCheck CLI – detect AWS service degradation early.")

@app.command()
def status(
    region: str = typer.Option(..., help="AWS region to check, e.g., us-east-1"),
    services: str = typer.Option("sns,sqs,s3", help="Comma-separated list of AWS services")
):
    """
    Check AWS service health for a region.
    """
    service_list = [s.strip().upper() for s in services.split(",")]
    results = core.check_services(region, service_list)
    
    for svc, state in results.items():
        if state == "OPERATIONAL":
            print(f"[green]✅ {svc}: {state}[/green]")
        else:
            print(f"[red]⚠️ {svc}: {state}[/red]")

if __name__ == "__main__":
    app()
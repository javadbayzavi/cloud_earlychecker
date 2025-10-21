def aws_cli_checker():
    """
    Check for AWS CLI installation.
    """
    import shutil
    if shutil.which("aws"):
        print("[green]AWS CLI is installed.[/green]")
    else:
        print("[red]AWS CLI is not installed. Please install it to proceed.[/red]")


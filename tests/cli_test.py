import pytest
from typer.testing import CliRunner
from aws_earlychecker.cli import app

runner = CliRunner()

def test_status_command():
    result = runner.invoke(app, ["status", "--region", "us-east-1"])
    assert result.exit_code == 0
    assert "OPERATIONAL" in result.output
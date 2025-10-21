from aws_earlychecker import core

def test_check_services():
    services = ["S3", "SNS"]
    results = core.check_services("us-east-1", services)
    assert all(svc in results for svc in services)
    assert all(results[svc] == "OPERATIONAL" for svc in services)
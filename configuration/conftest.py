import pytest
import smtplib

@pytest.fixture(scope="function",autouse="True")
def setup():
    print("Fixture Starts")
    yield
    print("Fixture Ends")

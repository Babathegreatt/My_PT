from typing import List
from configuration import conftest

import pytest

@pytest.fixture(scope="function",autouse="True")
def setup():
    print("Fixture Starts")
    yield
    print("Fixture Ends")

#@pytest.mark.usefixtures("setup")
class Test_One():

    def test_login(self):
        print("This is test 1")


class Test_Two():

    login_details = [["Dan", "pwd"]]

    @pytest.mark.parametrize("username, password", login_details)
    def test_second(self, username,password ):
        print("This is login 2")
        print(username)
        print(password)

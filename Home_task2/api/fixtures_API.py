import random
import pytest

from api.Client import Client
from data.Data import EMAIL, PASSWORD


@pytest.fixture(scope='function')
def api_client():
    user = EMAIL
    password = PASSWORD
    return Client(user, password)


@pytest.fixture(scope="function")
def create_name_of_segment_for_add():
    return "MySegmentFromAPI" + str(random.randint(0, 1000))


@pytest.fixture(scope="function")
def create_name_of_segment_for_delete():
    return "MySegmentFromAPI" + str(random.randint(-1000, -1))

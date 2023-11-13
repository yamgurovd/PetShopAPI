import os
import random
import pytest
from src.http_client import loger

seed = random.seed


@pytest.fixture()
def seed_for_test():
    return seed


@pytest.fixture(autouse=True)
def delete_logger_file():
    file_name = loger.file_name

    yield file_name

    os.remove(file_name)

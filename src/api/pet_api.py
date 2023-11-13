import os
from src.consts import POST_METHOD, GET_METHOD, PUT_METHOD
from src.http_client import HttpClient
from requests import Request
from src.checker import checker
from dotenv import load_dotenv

load_dotenv()

pet_api_client = HttpClient(base_url=os.getenv("BASE_URL"))


def create_pet(
        pet_id: int,
        category_id: int,
        pet_name: str = None,
        category_name: str = "dog",
        status: str = "available",
) -> dict:
    """Создание питомца"""

    request = Request(
        method=POST_METHOD,
        url="/pet",
        json={
            "id": pet_id,
            "category": {"id": category_id, "name": category_name},
            "name": pet_name,
            "status": status,
        },
    )
    response = pet_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)


def update_pet_data(
        pet_id: int,
        category_id: int,
        pet_name: str = None,
        category_name: str = "dog",
        status: str = "available",
) -> dict:
    """Изменение данных питомца"""

    request = Request(
        method=PUT_METHOD,
        url="/pet",
        json={
            "id": pet_id,
            "category": {"id": category_id, "name": category_name},
            "name": pet_name,
            "status": status,
        },
    )
    response = pet_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)


def find_pet(pet_id: int) -> dict:
    """Поиск пользователя по id"""

    request = Request(method=GET_METHOD, url=f"/pet/{pet_id}")

    response = pet_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)

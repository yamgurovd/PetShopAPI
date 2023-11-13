import os
from src.consts import POST_METHOD, GET_METHOD, PUT_METHOD
from src.http_client import HttpClient
from requests import Request
from src.checker import checker
from dotenv import load_dotenv

load_dotenv()

user_api_client = HttpClient(base_url=os.getenv("BASE_URL"))


def create_user(
        user_id: int,
        username: str,
        firstName: str,
        lastName: str,
        email: str,
        password: str,
        phone: str,
        userStatus: int = 0,
) -> dict:
    """Создание нового пользователя"""

    request = Request(
        method=POST_METHOD,
        url="/user",
        json={
            "id": user_id,
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": userStatus,
        },
    )

    response = user_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)


def find_user(username: str) -> dict:
    """Поиск пользователя по username"""

    request = Request(method=GET_METHOD, url=f"/user/{username}")
    response = user_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)


def update_user_data(
        user_id: int,
        username: str,
        firstName: str,
        lastName: str,
        email: str,
        password: str,
        phone: str,
        userStatus: int = 0,
) -> dict:
    """Изменение данных параметров выбранного пользователя"""

    request = Request(
        method=PUT_METHOD,
        url=f"/user{username}",
        json={
            "id": user_id,
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "password": password,
            "phone": phone,
            "userStatus": userStatus,
        },
    )

    response = user_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)

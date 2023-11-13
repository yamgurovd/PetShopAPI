import os
from src.consts import GET_METHOD
from src.http_client import HttpClient
from requests import Request
from src.checker import checker
from dotenv import load_dotenv

load_dotenv()

auth_api_client = HttpClient(base_url=os.getenv("BASE_URL"))


def user_login(username: str, password: str) -> dict:
    request = Request(
        method=GET_METHOD,
        url=f"/user/login?username={username}&password={password}"
    )

    response = auth_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)


def user_logout() -> dict:
    request = Request(
        method=GET_METHOD,
        url=f"/user/logout"
    )

    response = auth_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)

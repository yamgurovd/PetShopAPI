import requests
from requests import Response


def positive_status_code(response: Response, status_code: list[int] = [200, 201]) -> dict:
    assert response.status_code in status_code, f"Actual status {response.status_code} not in list {status_code}"

    return response.json()


def negative_status_code(response: Response, status_code: list[int] = [400, 405]) -> dict:
    assert response.status_code in status_code, f"Actual status {response.status_code} not in list {status_code}"

    return response.json()


def id_and_name_in_response(response: Response, pet_id: int, pet_name: str) -> None:
    assert response.json().get("id", "There is no key") == pet_id, \
        f'Actual pet id {response.json().get("id", "There is no key")} not equal expected pet id {pet_id}'

    assert response.json().get("name", "There is no key") == pet_name, \
        f'Actual pet name {response.json().get("name", "There is no key")} not equal expected pet name {pet_name}'

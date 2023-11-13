import os
import random
from src.consts import POST_METHOD, GET_METHOD, DELETE_METHOD
from src.http_client import HttpClient
from requests import Request
from src.checker import checker
import datetime
from dotenv import load_dotenv
from datas import ramdom_values, randomizer

load_dotenv()

store_api_client = HttpClient(base_url=os.getenv("BASE_URL"))


def create_order(
        order_id: int,
        pet_id: int,
        quantity: int = None,
        ship_date: datetime = str(datetime.datetime.now()),
        status: str = "placed",
        complete: bool = True
) -> dict:
    """Find an order for pet"""

    request = Request(
        method=POST_METHOD,
        url="/store/order",
        json={
            "id": order_id,
            "petId": pet_id,
            "quantity": quantity,
            "shipDate": ship_date,
            "status": status,
            "complete": complete
        }
    )

    response = store_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)


def find_purchase_in_order(order_id: int = random.randint(1, 10)) -> dict:
    """Place an order for pet"""

    request = Request(
        method=GET_METHOD,
        url=f"/store/order/{order_id}"
    )

    response = store_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)


def delete_purchase_in_order(order_id: int) -> dict:
    """Delete purchase order by id"""

    request = Request(
        method=DELETE_METHOD,
        url=f"/store/order/{order_id}"
    )

    response = store_api_client.send_request(request=request)

    return checker.positive_status_code(response=response)



import allure
import pytest
from src.api import order_store_api
from datas import randomizer
from src.checker import asserts
from datas import ramdom_values
from allure import severity, severity_level


@pytest.mark.parametrize(
    ("ship_date", "status"),
    [
        pytest.param(
            randomizer.random_choice(ramdom_values.ship_date_positive),
            randomizer.random_choice(ramdom_values.status_order_positive),
        )
    ],
    ids=["Create order positive"],
)
@severity(severity_level=severity_level.BLOCKER)
@allure.tag("smoke")
@allure.suite("New order")
@allure.title("Тест на создание очереди покупки в PetStore")
def test_create_order(ship_date, status, delete_logger_file):
    """
    1. Создаем новую запись очереди заказа в PetStore
    """

    with allure.step("Create new order in PetStore and check data"):
        new_order = order_store_api.create_order(
            order_id=ramdom_values.random_int_3_digit,
            pet_id=ramdom_values.random_int_3_digit,
            quantity=ramdom_values.random_int_3_digit,
            ship_date=randomizer.random_choice(ramdom_values.ship_date_positive),
            status=status,
            complete=True,
        )

        expected_result = [
            ramdom_values.random_int_3_digit,
            status,
        ]

        actual_result_post = [
            new_order.get("quantity", "testDefault"),
            new_order.get("status", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_post,
            expected_result=expected_result,
            message="Expected created user data not equal",
        )


@pytest.mark.parametrize(
    ("ship_date", "status"),
    [
        pytest.param(
            randomizer.random_choice(ramdom_values.ship_date_positive),
            randomizer.random_choice(ramdom_values.status_order_positive),
        )
    ],
    ids=["Delete created order positive"],
)
@severity(severity_level=severity_level.NORMAL)
@allure.tag("regress")
@allure.suite("New order")
@allure.title("Тест на создание очереди покупки в PetStore")
def test_delete_order(ship_date, status, delete_logger_file):
    """
    1. Создаем новую запись очереди заказа в PetStore
    2. Ищем созданную запись по id и проверяем данные
    3. Удаляем созданную запись по id и проверяем данные, что удалилось
    """

    with allure.step("Crete new order in PetStore and check data"):
        new_order = order_store_api.create_order(
            order_id=ramdom_values.random_int_3_digit,
            pet_id=ramdom_values.random_int_3_digit,
            quantity=ramdom_values.random_int_3_digit,
            ship_date=randomizer.random_choice(ramdom_values.ship_date_positive),
            status=status,
            complete=True,
        )
        order_id_ = new_order.get("id", "testDefault")

        expected_result = [
            ramdom_values.random_int_3_digit,
            status,
        ]

        actual_result_post = [
            new_order.get("quantity", "testDefault"),
            new_order.get("status", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_post,
            expected_result=expected_result,
            message="Expected created order data not equal",
        )

    with allure.step("Check order data in GET method"):
        founded_order = order_store_api.find_purchase_in_order(order_id=order_id_)

        actual_result_get = [
            founded_order.get("quantity", "testDefault"),
            founded_order.get("status", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_get,
            expected_result=expected_result,
            message="Expected founded order data not equal",
        )

    with allure.step("Delete created order and check data"):
        deleted_order = order_store_api.delete_purchase_in_order(order_id=order_id_)

        actual_result_delete = [
            deleted_order.get("code", "testDefault"),
            deleted_order.get("type", "testDefault"),
            deleted_order.get("message", "testDefault"),
        ]
        expected_result_delete = [
            200,
            "unknown",
            f"{order_id_}",
        ]

        asserts.equal(
            actual_result=actual_result_delete,
            expected_result=expected_result_delete,
            message="Expected deleted order data not equal",
        )

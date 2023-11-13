import allure
import pytest
from src.api import user_api
from datas import randomizer, ramdom_values
from src.checker import asserts
from allure import severity, severity_level


@pytest.mark.parametrize(
    (
            "username",
            "firstName",
            "lastName",
            "email",
            "password",
            "phone",
    ),
    [
        pytest.param(
            randomizer.random_choice(ramdom_values.username_list_positive),
            randomizer.random_choice(ramdom_values.firstname_list_positive),
            randomizer.random_choice(ramdom_values.lastname_list),
            randomizer.random_choice(ramdom_values.email_list_positive),
            randomizer.random_choice(ramdom_values.password_list_positive),
            randomizer.random_choice(ramdom_values.phone_list_positive),
        )
    ],
    ids=["Add new user positive"],
)
@severity(severity_level=severity_level.CRITICAL)
@allure.tag("smoke")
@allure.suite("New user")
@allure.title("Тест на создание нового пользователя")
def test_create_new_user(username, firstName, lastName, email, password, phone, delete_logger_file):
    """
    1. Создаем нового пользователя и проверяем его данные
    """
    with allure.step("Generate user and check data"):
        new_user = user_api.create_user(
            user_id=ramdom_values.random_int_3_digit,
            username=username,
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            phone=phone,
        )

        expected_result = [
            200,
            "unknown",
            f"{ramdom_values.random_int_3_digit}",
        ]

        actual_result_post = [
            new_user.get("code", "testDefault"),
            new_user.get("type", "testDefault"),
            new_user.get("message", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_post,
            expected_result=expected_result,
            message="Expected created user data not equal",
        )


@pytest.mark.parametrize(
    (
            "username",
            "firstName",
            "lastName",
            "email",
            "password",
            "phone",
    ),
    [
        pytest.param(
            randomizer.random_choice(ramdom_values.username_list_positive),
            randomizer.random_choice(ramdom_values.firstname_list_positive),
            randomizer.random_choice(ramdom_values.lastname_list),
            randomizer.random_choice(ramdom_values.email_list_positive),
            randomizer.random_choice(ramdom_values.password_list_positive),
            randomizer.random_choice(ramdom_values.phone_list_positive),
        )
    ],
    ids=["Update user data positive"]
)
@severity(severity_level=severity_level.MINOR)
@allure.tag("Regress")
@allure.suite("New user")
@allure.title("Тест на обновление данных созданного пользователя")
def test_update_user_data(username, firstName, lastName, email, password, phone, delete_logger_file):
    """
    1. Создаем нового пользователя и проверяем его данные
    2. Обновляем данные созданного пользователя и проверяем их
    3. Ищем созданного пользователя с обновленными данными и проверяем их
    """

    with allure.step("Generate user and check data"):
        new_user = user_api.create_user(
            user_id=ramdom_values.random_int_3_digit,
            username=username,
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            phone=phone,
        )

        expected_result = [
            200,
            "unknown",
            f"{ramdom_values.random_int_3_digit}",
        ]

        actual_result_post = [
            new_user.get("code", "testDefault"),
            new_user.get("type", "testDefault"),
            new_user.get("message", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_post,
            expected_result=expected_result,
            message="Expected created user data not equal",
        )

    with allure.step("Update user data and check ones"):
        updated_data_user = user_api.update_user_data(
            user_id=ramdom_values.random_int_3_digit,
            username="Ivan123",
            firstName="ivan",
            lastName="Sergeev",
            email="Sergeev.i@gmail.com",
            password="123ABC",
            phone="89171556900",
        )

        actual_result_put = [
            updated_data_user.get("code", "testDefault"),
            updated_data_user.get("type", "testDefault"),
            updated_data_user.get("message", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_put,
            expected_result=expected_result,
            message="Expected updated user data not equal",
        )

    with allure.step("Check updated user data in method GET"):
        founded_user = user_api.find_user(username="Ivan123")

        expected_result_get = [
            "Ivan123",
            "ivan",
            "Sergeev",
            "Sergeev.i@gmail.com",
            "123ABC",
            "89171556900",
        ]

        actual_result_get = [
            founded_user.get("username", "testDefault"),
            founded_user.get("firstName", "testDefault"),
            founded_user.get("lastName", "testDefault"),
            founded_user.get("email", "testDefault"),
            founded_user.get("password", "testDefault"),
            founded_user.get("phone", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_get,
            expected_result=expected_result_get,
            message="Expected updated user data not equal",
        )

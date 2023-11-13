import allure
import pytest
from src.api import user_api, auth_api
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
    ids=["User login positive"],
)
@severity(severity_level=severity_level.CRITICAL)
@allure.tag("smoke")
@allure.suite("New user")
@allure.title("Тест на выполнение авторизации пользователя")
def test_create_new_user(username, firstName, lastName, email, password, phone, delete_logger_file):
    """
    1. Создаем нового пользователя и проверяем его данные
    2. Выполняем авторизацию пользовательскими данными и проверяем, что авторизация выполнена
    """
    with allure.step("Create new user and check data"):
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

    with allure.step("Login in crated user and check data"):
        login_user = auth_api.user_login(
            username=username,
            password=password,
        )

        message = login_user.get("message", "testDefault")

        expected_result_login = [
            200,
            "unknown",
        ]

        actual_result_login = [
            login_user.get("code", "testDefault"),
            login_user.get("type", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_login,
            expected_result=expected_result_login,
            message="Expected login user data not equal",
        )

        asserts.word_in_text(
            actual_result=message,
            expected_result="logged in user session:",
            message="Words not in text",
        )

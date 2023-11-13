import allure
import pytest
from src.api import pet_api
from datas import randomizer, ramdom_values
from src.checker import asserts
from allure import severity, severity_level


@pytest.mark.parametrize(
    (
            "category_name",
            "pet_name",
    ),
    [
        pytest.param(
            randomizer.random_choice(ramdom_values.category_name_list_positive),
            randomizer.random_choice(ramdom_values.pet_name_list),
        ),
    ],
    ids=["Create new pet positive"]
)
@severity(severity_level=severity_level.MINOR)
@allure.tag("smoke")
@allure.suite("New pet")
@allure.title("Тест на создание нового питомца")
def test_create_new_pet(category_name, pet_name, delete_logger_file):
    """
    1. Создаем нового питомца и проверяем его данные
    """

    with allure.step("Create new pet and check data"):
        new_pet = pet_api.create_pet(
            pet_id=ramdom_values.random_int_3_digit,
            category_id=ramdom_values.random_int_minus_2_digit,
            category_name=category_name,
            pet_name=pet_name,
        )

        expected_result = [
            ramdom_values.random_int_3_digit,
            ramdom_values.random_int_minus_2_digit,
            category_name,
            pet_name,
        ]

        actual_result = [
            new_pet.get("id", "testDefault"),
            new_pet.get("category", "testDefault").get("id", "testDefault"),
            new_pet.get("category", "testDefault").get("name", "testDefault"),
            new_pet.get("name", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result,
            expected_result=expected_result,
            message="Expected data not equal",
        )


@pytest.mark.parametrize(
    (
            "category_name",
            "pet_name",
    ),
    [
        pytest.param(
            randomizer.random_choice(ramdom_values.category_name_list_positive),
            randomizer.random_choice(ramdom_values.pet_name_list),
        ),
    ],
    ids=["Update pet data positive"]
)
@allure.tag("Regress")
@allure.suite("New pet")
@allure.title("Тест на обновление данных созданного питомца")
def test_update_pet_data(category_name, pet_name, delete_logger_file):
    """
    1. Создаем нового питомца и проверяем его данные
    2. Обновление данных созданного питомца и проверка его данных
    3. Поиск созданного питомца с обновленными данными и проверка данных
    """
    with allure.step("Create new pet and check data"):
        new_pet = pet_api.create_pet(
            pet_id=ramdom_values.random_int_3_digit,
            category_id=ramdom_values.random_int_minus_2_digit,
            category_name=category_name,
            pet_name=pet_name,
        )
        pet_id_ = new_pet.get("id", "testDefault")

        expected_result_post = [
            ramdom_values.random_int_3_digit,
            ramdom_values.random_int_minus_2_digit,
            category_name,
            pet_name,
        ]

        actual_result_post = [
            new_pet.get("id", "testDefault"),
            new_pet.get("category", "testDefault").get("id", "testDefault"),
            new_pet.get("category", "testDefault").get("name", "testDefault"),
            new_pet.get("name", "testDefault"),
        ]

        asserts.equal(
            actual_result=actual_result_post,
            expected_result=expected_result_post,
            message="Expected created data not equal",
        )

    with allure.step("Update pet data and check ones"):
        pet_updated_data = pet_api.update_pet_data(
            pet_id=pet_id_,
            category_id=ramdom_values.random_int_3_digit,
            category_name="cat",
            pet_name="Murka",
        )

        expected_result_put = [
            pet_id_,
            ramdom_values.random_int_3_digit,
            "cat",
            "Murka",
        ]

        actual_result_put = [
            pet_updated_data.get("id", "testDefault"),
            pet_updated_data.get("category", "testDefault").get("id", "testDefault"),
            pet_updated_data.get("category", "testDefault").get("name", "testDefault"),
            pet_updated_data.get("name", "There is no key"),
        ]

        asserts.equal(
            actual_result=actual_result_put,
            expected_result=expected_result_put,
            message="Expected updated data not equal",
        )

    with allure.step("Check updated pet data in GET method"):

        founded_pet = pet_api.find_pet(pet_id=pet_id_)

        expected_result_put = [
            ramdom_values.random_int_3_digit,
            "cat",
            "Murka",
        ]

        actual_result_put = [
            founded_pet.get("category", "testDefault").get("id", "testDefault"),
            founded_pet.get("category", "testDefault").get("name", "testDefault"),
            founded_pet.get("name", "There is no key"),
        ]

        asserts.equal(
            actual_result=actual_result_put,
            expected_result=expected_result_put,
            message="Expected founded data not equal",
        )

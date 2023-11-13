import random
import datetime

random_int_minus_2_digit = random.randint(-100, -1)
random_int_2_digit = random.randint(1, 100)
random_int_3_digit = random.randint(1, 1000)
random_int_7_digit = random.randint(1000000, 2000000)
random_int_10_digit = random.randint(100000000, 200000000)
random_int3 = random.randint(1, 10)

# Данные для питомца
pet_name_list = [
    f"Murka{random_int_3_digit}",
    f"Тузик{random_int_minus_2_digit}",
    f"Рыjik{random_int_7_digit}",
]
pet_name_list_negative = [
    random_int_3_digit,
    0,
    random_int_minus_2_digit,
    None,
    "",
    bool,
]

category_name_list_positive = ["dog", "cat", "horse"]
category_name_list_negative = [" ", None, random_int3, bool, random_int_minus_2_digit]

status_list_positive = ["available", "pending", "sold"]
status_list_negative = [random_int_3_digit, random_int_minus_2_digit, "", None, bool]

# # Данные для пользователя
username_list_positive = [
    f"Ivanchic{random_int_3_digit}",
    f"Сергейчик{random_int_minus_2_digit}",
]
username_list_negative = [
    "",
    random_int_7_digit,
    0,
    random_int_minus_2_digit,
    None,
    bool,
]

firstname_list_positive = [
    f"Ivan{random_int_3_digit}",
    f"Сергей{random_int_minus_2_digit}",
]
firstname_list_negative = [
    "",
    random_int_3_digit,
    0,
    random_int_minus_2_digit,
    None,
]

lastname_list = [
    f"Ivanov{random_int_3_digit}",
    f"Петров{random_int_minus_2_digit}",
    f"Denisov{random_int_7_digit}",
]

email_masks = ["ru", "com", "org", "ру"]
email_submasks = ["gmail", "email", "outlook"]

email_list_positive = [
    f"Ivanov{random_int_3_digit}@{random.choice(email_submasks)}.{random.choice(email_masks)}",
    f"Sergeev_{random_int_10_digit}.@{random.choice(email_submasks)}.{random.choice(email_masks)}",
    f"Pavlov{random_int_minus_2_digit}@{random.choice(email_submasks)}.{random.choice(email_masks)}",
]

email_list_negative = [
    f"Ivanov{random_int_3_digit}",
    None,
    random_int3,
    random_int_minus_2_digit,
    " ",
]

password_list_positive = [
    "AbC",
    f"АбВ{random_int_10_digit}",
    f"!?р{random_int_minus_2_digit}",
]
password_list_negative = [random_int_minus_2_digit, None, random_int3, " "]

phone_masks_mobile = ["965", "917", "727"]
phone_masks_city = ["843", "844", "499"]

phone_list_positive = [
    f"8{random.choice(phone_masks_mobile)}{random_int_7_digit}",
    f"+7{random.choice(phone_masks_city)}{random_int_7_digit}",
    f"7{random.choice(phone_masks_mobile)}{random_int_7_digit}",
]

phone_list_negative = [
    f"8{random.choice(phone_masks_mobile)}{random_int_10_digit}",
    f"+7{random.choice(phone_masks_city)}{random_int_3_digit}",
    0,
    "",
    None,
    f"7{random_int_minus_2_digit}",
]

# Данные для покупки в petStore
ship_date_positive = [
    "2023-11-05T19:40:32.386Z",
]
ship_date_negative = ["test", bool]
order_status_negative = [random_int_3_digit, bool, random_int_minus_2_digit]
quantity_negative = [" ", bool, random_int_minus_2_digit]
status_order_positive = [
    "placed",
    "unplaced",
]

"""Створюємо функцію, яка нормалізує номер телефону"""

# імпортуємо модуль re
import re

# створюємо функцію
def normalize_phone(raw_numbers):

    # видаляємо неприпустимі символи
    pattern = r"[^0-9]"
    replacement = ""
    modified_text = re.sub(pattern, replacement, raw_numbers).lstrip("38")

    # замінюємо нульове значення на +380
    pattern = r"^0"
    replacement = "+380"
    modified_text = re.sub(pattern, replacement, modified_text)

    # повертаємо нормалізований текст та перевіряємо правильність введення
    if len(modified_text) == 13:
        return modified_text
    else:
        print("Incorrect phone number " + raw_numbers)
        return None

# отримуємо вхідні дані
raw_numbers = [
    "067\\t123 4567",
    "(095) 234+5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# викликаємо функцію
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]\

# виводимо нормалізовані номери
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
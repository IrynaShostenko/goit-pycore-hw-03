"""Пишемо функцію, яка допоможе генерувати набір унікальних випадкових чисел для лотереї"""
# імпортуємо модуль random
import random

# створюємо функцію
def get_numbers_ticket(min, max, quantity):

    # перевіряємо правильність введення
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)

        # генеруємо набір чисел
        lottery_numbers = random.sample(range(min, max + 1), quantity)

        # сортуємо набір чисел
        lottery_numbers.sort()

        # повертаємо набір чисел
        return lottery_numbers
    
    # якщо є помилка, повертаємо порожній список
    except ValueError:
        print("Incorrect data format, should be integer")
        return []
    
    except Exception as e:
        print(e)
        return []

# викликаємо функцію
lottery_numbers = get_numbers_ticket(1, 49, 6)

# виводимо набір чисел  
print("Ваші лотерейні числа:", lottery_numbers)

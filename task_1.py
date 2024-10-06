"""Створюємо функцію, яка розраховує кількість днів між заданою датою та поточною датою"""

# імпортуємо модуль datetime
from datetime import datetime

# створюємо функцію
def get_days_from_today(date):
    # перевіряємо правильність введення дати
    try:
        # перетворюємо введену дату в форматі 'РРРР-ММ-ДД' у об'єкт datetime
        date = datetime.strptime(date, "%Y-%m-%d").date()

    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
    
    # отримуємо поточну дату
    today = datetime.today().date()

    # рахуємо кількість днів між датами
    return (today - date).days
# отримуємо дату
date = ("1983-09-15")

# викликаємо функцію                        
print(get_days_from_today(date))
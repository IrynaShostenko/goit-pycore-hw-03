"""створюємо функцію, яка допоможе визначати, кого з колег потрібно привітати."""

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):

    # визначаємо поточну дату
    today = datetime.today().date()
    
    # визначаємо дату наступного тижня
    next_week = today + timedelta(days=7)

    # визначаємо дату понеділка наступного тижня
    first_day_of_next_week = next_week - timedelta(days=next_week.weekday())

    # створюємо список привітань
    upcoming_birthdays = []

    # перебираємо користувачів
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congratulation_date = user_birthday.replace(year=today.year)

        # визначаємо дату привітання
        if congratulation_date < today:
            congratulation_date = user_birthday.replace(year=today.year + 1)

        if congratulation_date >= today and congratulation_date <= next_week:
            if congratulation_date.weekday() <= 4:
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})
            elif congratulation_date.weekday() == 5 or 6:
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": first_day_of_next_week.strftime("%Y.%m.%d")})
      
    # повертаємо список привітань
    return upcoming_birthdays

# отримуємо вхідні дані
users = [
    {"name": "John Doe", "birthday": "1985.10.08"},
    {"name": "Jane Smith", "birthday": "1990.10.11"},
    {"name": "Bob Johnson", "birthday": "1995.10.13"},
    {"name": "Alice Williams", "birthday": "1988.02.02"},
    {"name": "Mike Brown", "birthday": "1992.01.01"},
]

# викликаємо функцію   
upcoming_birthdays = get_upcoming_birthdays(users)

# виводимо список привітань на цей та наступний тиждень
print("Список привітань на цьому тижні:", sorted(upcoming_birthdays, key=lambda dates: dates["congratulation_date"]))
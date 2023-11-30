from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(user_list):
    today = datetime.today().date()
    birthdays = defaultdict(list)
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    for user in user_list:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year) if birthday.replace(
            year=today.year) >= today else birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days < 7:
            day_of_week = days_of_week[birthday_this_year.weekday()]
            day_of_week = 'Monday' if day_of_week in ['Saturday', 'Sunday'] else day_of_week
            birthdays[day_of_week].append(name)

    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")


users_data = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Steve Jobs", "birthday": datetime(1955, 2, 24)},
]

get_birthdays_per_week(users_data)

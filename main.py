from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        return (datetime.today() - date).days
    except Exception:    
        return print("Введіть дату у форматі ''РРРР-ММ-ДД'")

print(get_days_from_today("2024-08-09"))   

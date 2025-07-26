from datetime import datetime

def get_days_from_today(date_str):
    try:
        today = datetime.today().date()
        date = datetime.strptime(date_str, "%Y-%m-%d").date
        return (today - date).days

    except ValueError:
        print("неправильний формат дати. Використовуйте YYYY-MM-DD.")
        return None


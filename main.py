from datetime import datetime

def get_days_from_today(date_str):
    try:
        today = datetime.today().date()
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return (today - date).days

    except ValueError:
        print("неправильний формат дати. Використовуйте YYYY-MM-DD.")
        return None
    

    
print("Різниця в днях:", get_days_from_today("2023/01/01"))

print("Різниця в днях:", get_days_from_today("2023-01-01"))



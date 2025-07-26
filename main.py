def get_days_from_today(date):
    from datetime import datetime
    today = datetime.today().date()
    date = datetime.strptime(date, "%Y-%m-%d").date()
    days_diff = (today - date).days
    return (today - date).days

print("Різниця в днях:", get_days_from_today("2023-01-01"))

    

from datetime import datetime, timedelta

def add_days():
    product_name = input("Name of Product: ")
    start_date = input("Starting date of the stability testing: (in YYYY-MM-DD format): ")
    start_date = datetime.strptime(start_date, "%Y-%m-%d")

    for i in range(5):
        new_date = start_date + timedelta(days=15 * (i + 1))
        print(f"Withdrawal dates are: {new_date.strftime('%Y-%m-%d')}")

add_days()
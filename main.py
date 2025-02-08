import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%y-%m-%d"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date","amount","category","description"])
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }

        with open(cls.CSV_FILE, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['date'] = (pd.to_datetime(df['date'], format='mixed'))
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        transaction_range = (df['date'] >= start_date) & (df['date'] <= end_date)
        filtered_df = df.loc[transaction_range]

        if filtered_df.empty:
            print("No transactions found for the given date range")
        else:
            filtered_df = filtered_df.sort_values(by=['date'])
            print(f"Transactions for the given date range {start_date} & {end_date}")

            print(
                filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)})
            )
            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expenses = filtered_df[filtered_df["category"] != "Income"]["amount"].sum()

            print("\nSummary :", )
            print("Total Income   : ", total_income)
            print("Total Expenses : ", total_expenses)
            print(f"Net Savings   : ${(total_income - total_expenses):.2f}")
            print("\n")




def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction ('dd-mm-yyyy') or enter for today's date : ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)
    print("Entry added successfully")


def plot_transactions():
    pass


def main():
    while True:
        print("1: Add a transaction")
        print("2: View transactions within a date range")
        print("3: Exit")
        choice = input("Enter your choice (1, 2, 3): ")
        if choice == "1":
           add()
        elif choice == "2":
            print("Enter date range")
            start_date = get_date("Enter the start date : ")
            print(start_date)
            end_date = get_date("Enter the end date : ")
            CSV.get_transactions(start_date, end_date)
        elif choice == "3":
            break


if __name__ == '__main__':
    main()


#add()
#CSV.get_transactions('24-01-28', '24-01-28')

#CSV.initialize_csv()
#CSV.add_entry('2025-01-27', 1000, 'Grocery','Food Items')

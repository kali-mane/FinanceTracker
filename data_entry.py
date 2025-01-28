from datetime import datetime

CATEGORY = {'I': 'Income', 'E': 'Expense'}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)

    if allow_default and not date_str:
        return datetime.today().strftime("%d-%m-%y")

    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%y")
    except ValueError:
        print("Invalid date format. Please enter date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount : "))
        if amount <= 0:
            raise ValueError("Amount must be non-negative, non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category('I' for income, 'E' for expense) : ")
    if category in CATEGORY:
        return CATEGORY[category]
    print("Invalid Category. Please enter 'I' for income, 'E' for expense")
    return get_category()

def get_description():
    return input("Enter description : ")





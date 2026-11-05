import csv
from datetime import date, timedelta
from pathlib import Path


today = str(date.today())
today_obj = date.today()
weeksrt = today_obj - timedelta(days=today_obj.weekday())
weekstart = str(weeksrt)
cmonth = date.today().strftime('%Y-%m')


def FirstTime():
    print("Welcome! Let's set up.\n\n" \
    "How often do you recieve your allowance?\n" \
    "1. Daily\n" \
    "2. Weekly\n" \
    "3. Monthly\n")

    freq = ''
    while True:

        freq_choice = 0

        try:
            freq_choice = int(input("Choice: "))
        except ValueError:
            print("\nChoose between 1 and 3.")            
        
        if freq_choice == 1:
            freq = 'Daily'
            break
        elif freq_choice == 2:
            freq = 'Weekly'
            break
        elif freq_choice == 3:
            freq = 'Monthly'
            break
        else:
            print("Invalid Choice")

    allow = 0
    while allow <= 0:
        try:
            allow = float(input("\nHow much is your allowance now?: "))
        except ValueError:
            print("\nPlease input a numerical value.")

        if allow <= 0:
            print("\nPlease provide a positive value!")

    bheaders = ["allowance", "frequency"]
    bdata = [allow, freq]

    bfilename = "budget.csv"

    # make budget.csv to store allowance amount and frequency
    with open(bfilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(bheaders)
        writer.writerow(bdata)

    # make expenses.csv for logging purposes
    eheaders = ["Date", "Amount", "Category", "Description"]
    efilename = "expenses.csv"

    with open(efilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(eheaders)

    print("\nSuccesfully set up your allowance tracking!\n" \
    "Run again to use the tracker.\n")


def updBudget():

    print("Updating your budget!\n\n" \
    "How often do you recieve your allowance now?\n" \
    "1. Daily\n" \
    "2. Weekly\n" \
    "3. Monthly\n")

    freq = ''
    while True:

        freq_choice = 0

        try:
            freq_choice = int(input("Choice: "))
        except ValueError:
            print("\nChoose between 1 and 3.")
        
        if freq_choice == 1:
            freq = 'Daily'
            break
        elif freq_choice == 2:
            freq = 'Weekly'
            break
        elif freq_choice == 3:
            freq = 'Monthly'
            break
        else:
            print("Invalid Choice")

    allow = 0
    while allow <= 0:
        try:
            allow = float(input("\nHow much is your allowance now?: "))
        except ValueError:
            print("\nPlease input a numerical value.")

        if allow <= 0:
            print("\nPlease provide a positive value!")


    bheaders = ["allowance", "frequency"]
    bdata = [allow, freq]

    bfilename = "budget.csv"

    # make budget.csv to store allowance amount and frequency
    with open(bfilename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(bheaders)
        writer.writerow(bdata)

    print("\n")


def MainMenu():
    print("============================\n" \
    "   Student Budget Tracker      \n" \
    "============================\n")

    print("1. View Budget\n" \
    "2. Log Expense\n" \
    "3. View Expenses\n" \
    "4. View Analytics\n" \
    "5. Update Allowance\n" \
    "6. Exit\n")


def LogExpense():
    print("====== Log Expense ======\n")

    amt = 0
    while amt <= 0:
        try:
            amt = float(input("Enter amount spent: "))
            if amt < 0:
                print("No negative numbers!!!")
        except ValueError:
            print("\nEnter a numerical value please.")


    print("\nSelect Category:\n" \
    "1. Food\n" \
    "2. Transportation\n" \
    "3. School Supplies\n" \
    "4. Entertainment\n" \
    "5. Personal\n" \
    "6. Other\n")

    cat = ""

    while cat == "":
        try:
            catchoice = int(input("Category: "))

            if catchoice == 1:
                cat = "Food"
            elif catchoice == 2:
                cat = "Transportation"
            elif catchoice == 3:
                cat = "School Supplies"
            elif catchoice == 4:
                cat = "Entertainment"
            elif catchoice == 5:
                cat = "Personal"
            elif catchoice == 6:
                cat = "Other"
            else:
                print("Invalid Choice.")
        except ValueError:
            print("\nPlease choose between 1 and 6.")
        
    desc = input("\nDescription: ")

    log = [today, amt, cat, desc]

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log)


def calculateBudget():

    allowance = []
    mode = []

    with open("budget.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            mode.append(row["frequency"])
            allowance.append(float(row["allowance"]))

    expenses = []

    with open("expenses.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if mode[0] == 'Daily':
                if row["Date"] == today:
                    expenses.append(float(row["Amount"]))
            if mode[0] == 'Weekly':
                if weekstart <= row["Date"] <= today:
                    expenses.append(float(row["Amount"]))
            if mode[0] == 'Monthly':
                if row["Date"].startswith(cmonth):
                    expenses.append(float(row["Amount"]))

    #print(expenses)
    fixed_allowance = sum(allowance)
    t_exp = sum(expenses)

    remaining = (fixed_allowance - t_exp)

    print("Remaining: ", remaining)


def compareExpenses():

    print("====== Spending Analysis ======")

    while True:
        print("Which comparison would you like to do?\n" \
        "1. Yesterday\n" \
        "2. Last Week\n" \
        "3. Last Month\n")

        mode = 0

        while mode == 0:
            try:
                mode = int(input("Choice: "))
            except ValueError:
                print("\nPlease select between 1 and 3.")

        if mode == 1:

            yesterday_obj = today_obj - timedelta(days=1)

            yesterday = str(yesterday_obj)

            t_expenses = []
            y_expenses = []

            with open("expenses.csv", mode='r', newline='') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row["Date"] == today:
                        t_expenses.append(float(row["Amount"]))
                    elif row["Date"] == yesterday:
                        y_expenses.append(float(row["Amount"]))

            t_total = sum(t_expenses)
            y_total = sum(y_expenses)

            print("\nToday")
            print("Spent: ", t_total)

            print("\nYesterday")
            print("Spent: ", y_total)

            print("")

            if t_total > y_total:
                print(f"You spent {t_total - y_total} more today.")
            elif y_total > t_total:
                print(f"You spent {y_total - t_total} less than yesterday!")
            else:
                print("You spent the same amount.")

            print('')
            break
            
        elif mode == 2:

            lweek_s = weeksrt - timedelta(days=7)
            lweek_e = weeksrt - timedelta(days=1)

            lweek_start = str(lweek_s)
            lweek_end = str(lweek_e)

            cweek_expenses = []
            lweek_expenses = []

            #print(weekstart)
            #print(lweek_start)

            with open("expenses.csv", mode='r', newline='') as file:
                reader = csv.DictReader(file)
            
                for row in reader:
                    if weekstart <= row["Date"] <= today:
                        cweek_expenses.append(float(row["Amount"]))
                    elif lweek_start <= row["Date"] <= lweek_end:
                        lweek_expenses.append(float(row["Amount"]))

            cweek_total = sum(cweek_expenses)
            lweek_total = sum(lweek_expenses)

            print("\nThis Week")
            print("Spent: ", cweek_total)     

            print("\nLast Week")
            print("Spent: ", lweek_total)                        

            print("")
            
            if cweek_total > lweek_total:
                print(f"You spent {cweek_total - lweek_total} more this week.")
            elif lweek_total > cweek_total:
                print(f"You spent {lweek_total - cweek_total} less than last week!")
            else:
                print("You spent the same amount.")

            break

        elif mode == 3:

            year, month = cmonth.split("-")
            year = int(year)
            month = int(month)

            if month == 1:
                last_month = f"{year - 1} - 12"
            else:
                last_month = f"{year}-{month - 1:02d}"

            month_exp = []
            lmonth_exp = []

            with open("expenses.csv", mode='r', newline='') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if row["Date"].startswith(cmonth):
                        month_exp.append(float(row["Amount"]))
                    elif row["Date"].startswith(last_month):
                        lmonth_exp.append(float(row["Amount"]))

            month_total = sum(month_exp)
            lmonth_total = sum(lmonth_exp)

            print("\nThis Month")
            print("Spent: ", month_total)     
            
            print("\nLast Month")
            print("Spent: ", lmonth_total)                        
            
            print("")
                        
            if month_total > lmonth_total:
                print(f"You spent {month_total - lmonth_total} more this month.")
            elif lmonth_total > month_total:
                print(f"You spent {lmonth_total - month_total} less than last month!")
            else:
                print("You spent the same amount.")

            break

        else:
            print("Invalid Choice.")


def viewExpenses():

    print("=" * 70)
    print(f"{'Date':<15}{'Category':<20}{'Amount':<15}{'Description':<20}")
    print("=" * 70)

    expenses = []

    with open("expenses.csv", mode='r', newline='') as file:
        reader = csv.reader(file)
    
        next(reader) # skip headers
    
        for row in reader:
            expenses.append(row)

    for expense in expenses:
        print(f"{expense[0]:<15}{expense[2]:<20}{expense[1]:<15}{expense[3]:<20}")
        print("=" * 70)

    print("\n")    


def goBack():

    print("\nGo to main menu?\n" \
    "1. Yes\n" \
    "2. Close\n")

    while True:

        back = 0 

        while back == 0:
            try:
                back = int(input("Choice: "))
            except ValueError:
                print("\nSelect 1 or 2.")

        if back == 1:
            return 0
        elif back == 2:
            print("Goodbye!")
            return 1
        else:
            print("Invalid Choice")


# actual system

close = 0
budget_file = Path("budget.csv")

if budget_file.is_file():
    while close == 0:
        print('')
        MainMenu()

        choice = 0

        try:
            choice = int(input("What would you like to do? : "))
        except ValueError:
            print("\nPlease select between 1 and 6.")

        if choice == 1:
            calculateBudget()
            close = goBack()
        elif choice == 2:
            LogExpense()
            close = goBack()
        elif choice == 3:
            viewExpenses()
            close = goBack()
        elif choice == 4:
            print("\n")
            compareExpenses()
            close = goBack()
        elif choice == 5:
            print("=" * 30)
            updBudget()
            close = goBack()
        elif choice == 6:
            close = 1
        else:
            print("Invalid Choice!")
else:
    FirstTime()

def upcoming_birthdays():
    today = input("Enter today's date (dd-mm): ")

    day, month = today.split("-")
    today = day + "-" + month

    file = open("birthdays.txt", "r")
    birthdays = file.readlines()
    file.close()

    upcoming_birthdays = []

    for line in birthdays:
        name, birth_date_str = line.split(",")
        birth_day, birth_month, _ = birth_date_str.split("-")

        birth_day = int(birth_day)
        birth_month = int(birth_month)
        day = int(day)
        month = int(month)

        if birth_month == month and (birth_day > day and birth_day <= day + 7):
            upcoming_birthdays.append((name, birth_date_str))
        elif birth_month > month:
            upcoming_birthdays.append((name, birth_date_str))

    if not upcoming_birthdays:
        print("No upcoming birthdays in the next 7 days ! ")
    else:
        print("\nUpcoming birthdays in the next 7 days Are :: \n")
        for name, birth_date in upcoming_birthdays:
            print(f"{name}'s birthday is on {birth_date}")


def birthday_reminder():

    print("Check Upcoming Birthdays ::  ")
    upcoming_birthdays()


birthday_reminder()

# calendar_maker.py
#   This program lets a user create a monthly calendar, saved to a text file
#   ready to print.
# by: Scott Gordon

import datetime

DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday,")
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

print("***** Calendar Maker *****")

# Loop to get the year from user
while True:
    print("Enter the year for the calendar:")
    response = input("> ")

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("Please enter a numeric year, i.e. 2028.")
    continue

# Loop to get the month from user
while True:
    print("Enter the month for the calendar, 1-12:")
    response = input("> ")

    if not response.isdecimal():
        print("Please enter a numeric month, i.e. 1 for January.")
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print("Please enter a number from 1 to 12.")


def get_calendar_for(year, month):
    cal_text = ""

    # Add month and year to top of calendar.
    cal_text += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

    # Add days of week labels to calendar.
    cal_text += """+----------+----------+----------+----------+----------+----------+----------+
|  Sunday  |  Monday  | Tuesday  |Wednesday | Thursday |  Friday  | Saturday |\n"""

    week_separator = ("+----------" * 7) + "+\n"
    blank_row = ("|          " * 7) + "|\n"

    # Get first date in month
    current_date = datetime.date(year, month, 1)

    # Roll back current_date until it's equal to Sunday.
    while current_date.weekday() != 6:
        current_date -= datetime.timedelta(days=1)

    while True:
        # Loop over each week in month
        cal_text += week_separator

        # Create row with day number labels
        day_number_row = ""
        for i in range(7):
            day_number_label = str(current_date.day).rjust(2)
            day_number_row += "|" + day_number_label + (" " * 8)
            # Go to next day
            current_date += datetime.timedelta(days=1)
        day_number_row += "|\n"

        # Add day number row and 3 black rows to calender text.
        cal_text += day_number_row
        for i in range(3):
            cal_text += blank_row

        # Check if done with month
        if current_date.month != month:
            break

    # Add horizontal line to bottom
    cal_text += week_separator
    return cal_text


cal_text = get_calendar_for(year, month)
print(cal_text)

# Save to text file
calendar_file_name = f"calendar_{year}_{month}.txt"
with open(calendar_file_name, "w") as file_obj:
    file_obj.write(cal_text)

print("Saved to " + calendar_file_name)

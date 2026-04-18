# CIRCADIA - A Python-Based Student Sleep Monitoring System
# "Track Better, Sleep Smarter"
# Authors : Travis Julian P. Fuentes
#           Emmbert Mattheiu O. Cebrian
#           Markellus Jhames D. Chu
# Section : Grade 7 - Turquoise

# Constants for time conversion
minutes_per_hour = 60
hours_per_day    = 24
minutes_per_day  = hours_per_day * minutes_per_hour


# FUNCTION: CheckDigits
# Checks whether every character in a string is a digit.
# Parameter:
#   text - the string to check
# Returns True if all characters are digits, False otherwise.
def CheckDigits(text):
    all_digits = True
    index      = 0

    while index < len(text):
        ch = text[index]
        if ch < "0" or ch > "9":
            all_digits = False
        index += 1

    return all_digits


# FUNCTION: GetAge
# Prompts the user until a valid non-negative integer age is entered.
# Returns the validated age as an integer.
def GetAge():
    valid = False
    age   = 0

    while not valid:
        raw = input("Enter your age in years: ")

        if raw == "":
            print("Invalid input! Please enter an integer.")
        elif not CheckDigits(raw):
            print("Invalid input! Please enter an integer.")
        else:
            age   = int(raw)
            valid = True

    return age


# FUNCTION: GetHour
# Prompts the user until a valid hour between 1 and 12 is entered.
# Parameter:
#   label - short label used in the prompt, e.g. "sleep" or "wake-up"
# Returns the validated hour as an integer.
def GetHour(label):
    valid = False
    hour  = 0

    while not valid:
        raw = input("Enter " + label + " hour (1-12): ")

        if raw == "":
            print("Invalid input! Please enter an integer.")
        elif not CheckDigits(raw):
            print("Invalid input! Please enter an integer.")
        else:
            hour = int(raw)

            if hour < 1 or hour > 12:
                print("Hour must be from 1 to 12.")
            else:
                valid = True

    return hour


# FUNCTION: GetMinute
# Prompts the user until a valid minute between 0 and 59 is entered.
# Parameter:
#   label - short label used in the prompt, e.g. "sleep" or "wake-up"
# Returns the validated minute as an integer.
def GetMinute(label):
    valid  = False
    minute = 0

    while not valid:
        raw = input("Enter " + label + " minute (0-59): ")

        if raw == "":
            print("Invalid input! Please enter an integer.")
        elif not CheckDigits(raw):
            print("Invalid input! Please enter an integer.")
        else:
            minute = int(raw)

            if minute < 0 or minute > 59:
                print("Minute must be from 0 to 59.")
            else:
                valid = True

    return minute


# FUNCTION: GetAmPm
# Prompts the user until "AM" or "PM" is entered.
# Returns the validated period string.
def GetAmPm(prompt):
    period = ""

    while period != "AM" and period != "PM":
        period = input(prompt)

        if period != "AM" and period != "PM":
            print("Invalid input! Please enter AM or PM.")

    return period


# FUNCTION: GetTimeInMinutes
# Collects a time from the user (period, hour, minute) and converts
# it to total minutes elapsed since midnight.
# Parameter:
#   label - short label used in prompts, e.g. "sleep" or "wake-up"
# Returns total minutes from midnight as an integer.
def GetTimeInMinutes(label):
    # Get AM/PM period
    period = GetAmPm("\nEnter " + label + " time period (AM/PM): ")

    # Get hour within 1-12
    hour = GetHour(label)

    # Get minute within 0-59
    minute = GetMinute(label)

    # Convert 12-hour clock to 24-hour clock
    if period == "AM":
        if hour == 12:
            hour_24 = 0       # 12:xx AM is midnight hour
        else:
            hour_24 = hour
    else:
        if hour == 12:
            hour_24 = 12      # 12:xx PM stays as 12
        else:
            hour_24 = hour + 12

    return hour_24 * minutes_per_hour + minute


# FUNCTION: GetRequiredHours
# Returns the minimum recommended sleep hours for a given age,
# based on standard pediatric sleep guidelines.
def GetRequiredHours(age):
    if age == 0:
        return 13
    elif age <= 2:
        return 12
    elif age <= 4:
        return 11
    elif age <= 6:
        return 10
    elif age <= 12:
        return 9
    elif age <= 17:
        return 8
    else:
        return 7   # Adults 18 and older


# FUNCTION: FormatDuration
# Converts a duration in minutes into a human-readable string.
# Examples: 90 -> "1 hour and 30 minutes", 60 -> "1 hour", 45 -> "45 minutes"
def FormatDuration(total_minutes):
    hours   = total_minutes // minutes_per_hour
    minutes = total_minutes  % minutes_per_hour

    # Build hour part with correct singular/plural grammar
    if hours == 1:
        hour_part = "1 hour"
    else:
        hour_part = str(hours) + " hours"

    # Build minute part with correct singular/plural grammar
    if minutes == 1:
        minute_part = "1 minute"
    else:
        minute_part = str(minutes) + " minutes"

    # Combine parts based on which values are non-zero
    if hours == 0 and minutes == 0:
        return "0 minutes"
    elif hours == 0:
        return minute_part
    elif minutes == 0:
        return hour_part
    else:
        return hour_part + " and " + minute_part


# MAIN PROGRAM

# Input: Name
fname = input("Enter first name: ")
lname = input("Enter last name: ")
print("\n----- PROGRAM START -----")
print("Hello,", fname, lname + "!")

# Input: Age
age = GetAge()

# Process: Determine required sleep based on age
required_hours   = GetRequiredHours(age)
required_minutes = required_hours * minutes_per_hour

# Input: Sleep and wake-up times
sleep_total_minutes = GetTimeInMinutes("sleep")
wake_total_minutes  = GetTimeInMinutes("wake-up")

# Process: Compute actual sleep duration
slept_minutes = wake_total_minutes - sleep_total_minutes

# A negative result means the person slept past midnight; wrap around
if slept_minutes < 0:
    slept_minutes = slept_minutes + minutes_per_day

# Process: Determine sleep status
if slept_minutes >= required_minutes:
    status_text = "Enough"
else:
    status_text = "Not Enough"

# Output: Sleep Duration Analysis
print("\n----- SLEEP DURATION ANALYSIS -----")
print("Sleep Duration:", FormatDuration(slept_minutes))
print("Status:", status_text)

# If sleep was insufficient, show how much more is needed
if status_text == "Not Enough":
    shortfall = required_minutes - slept_minutes
    print("Suggestion: Try sleeping", FormatDuration(shortfall), "earlier")

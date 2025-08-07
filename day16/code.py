# day-16
import datetime as dt

###exercice
# 1
current_time = dt.datetime.now()
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.timestamp)


# 2
formated_date = current_time.strftime("%m/%d/%Y, %H:%M:%S")
print(formated_date)

# 3
string_date = "5 December, 2019"
obtained_date = dt.datetime.strptime(string_date, "%d %B, %Y")
print(obtained_date)

# 4
diff_new_year_now = dt.date(2026, 1, 1) - dt.date.today()
print(diff_new_year_now)

# 5
diff_now_old_time = dt.date.today() - dt.date(1970, 1, 1)
print(diff_now_old_time)

# 6: there are a lot of thing we can do with datetime module in python
# Parsing and formatting: Convert between strings and datetime objects (logs, filenames, user input).
# Time arithmetic: Add/subtract periods (deadlines, expirations, reminders, cooldowns).
# Time series workflows: Windowing, resampling anchors, and indexing when combined with data tools.
# Scheduling and reminders
# Timezone conversions
# Reporting: Period boundaries (start/end of day, week, month, quarter, year).

import datetime as dt

# day-15
###exercice
# 1
current_time = dt.datetime.now()
print(current_time)

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

# 6
# TODO: unclear instructions

### exercice-level 1
# 1
REF_AGE = 18
user_age = int(input("Enter your age: "))
if user_age > REF_AGE:
    print("You are old enough to learn to drive.")
else:
    remaining_age = REF_AGE - user_age
    print(f"You need {remaining_age} more years to learn to drive.")
# 2
MY_AGE = 22
your_age = int(input("Enter your age: "))

diff_year = abs(MY_AGE - your_age)
diff_message = f"{diff_year} year" if diff_year == 1 else f"{diff_year} years"
if MY_AGE > your_age:
    print(f"I am {diff_message} older than you")
else:
    print(f"You are {diff_message} older than me")
# 3
number_1 = eval(input("Enter number one: "))
number_2 = eval(input("Enter number two: "))
if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
elif number_1 < number_2:
    print(f"{number_1} is lower than {number_2}")
else:
    print(f"{number_1} is equal to {number_2}")

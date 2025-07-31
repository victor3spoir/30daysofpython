### exercice level 2
# 1
score = int(input("Enter your score: "))

if 0 <= score < 49:
    grade = "F"
elif 50 <= score < 59:
    grade = "D"
elif 60 <= score < 69:
    grade = "C"
elif 70 <= score < 89:
    grade = "B"
else:
    grade = "A"
print(grade)


# 2
month_season = {
    "September": "Autumn",
    "October": "Autumn",
    "November": "Autumn",
    "December": "Winter",
    "January": "Winter",
    "February": "Winter",
    "March": "Spring",
    "April": "Spring",
    "May": "Spring",
    "June": "Summer",
    "July": "Summer",
    "August": "Summer",
}

month = input("Please, enter a month name: (eg:March): ").strip().capitalize()
print(
    "The current season is: ",
    month_season.get(month, "🙄euuh, Unknown season for the unknown month you entered"),
)

# 3
fruits = ["banana", "orange", "mango", "lemon"]
fruit_name = input("Enter a name for fruit: ")
if fruit_name in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit_name)
    print(fruits)

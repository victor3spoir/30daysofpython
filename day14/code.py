###day-14

##exercice-1
import functools
import typing
from countries import countries as countries_v2
from countries_data import countries_data

countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1
# map change data, filter keep only those which fit the criteria, et reduce combine all item together

# 2
# high order function: function that take another function as parameter
# closure: maintain state that is used with another variable later
# decorator: kind of high order function that wrap another function & change it behavior


# 3
def square(number: int):
    return number * 2


def is_even(number: int):
    return number % 2 == 0


def add(n1: int, n2: int):
    return n1 + n2


print(list(map(square, numbers)))
print(list(filter(is_even, numbers)))
print(functools.reduce(add, numbers, 0))

# 4
for country in countries:
    print(country)

# 5
for name in names:
    print(name)
# 6
for number in numbers:
    print(number)


##exercice 2
# 1
upper_countries = list(map(lambda x: x.upper(), countries))
print(upper_countries)

# 2
square_numbers = list(map(square, numbers))
print(square_numbers)

# 3
upper_names = list(map(lambda x: x.upper(), names))

# 4
land_countries = list(filter(lambda x: x.lower().endswith("land"), countries))
print(land_countries)

# 5
sixchar_countries = list(filter(lambda x: len(x) == 6, countries))
print(sixchar_countries)
# 6
sixchar_and_more_countries = list(filter(lambda x: len(x) == 6, countries))
print(sixchar_and_more_countries)

# 7
start_with_e_countries = list(filter(lambda x: x.upper().startswith("E"), countries))

# 8
chainin_operation = functools.reduce(
    lambda x, y: x + y, filter(lambda e: e % 3 == 0, map(lambda x: x**3, numbers))
)
print(chainin_operation)


# 9
def get_string_lists(data: list[typing.Any]):
    return list(filter(lambda x: type(x) == str, data))


print(get_string_lists([8, 8, "dfss", "88", "dsfdsfds", 8, 8887]))

# 10
print(functools.reduce(lambda x, y: x + y, numbers))

# 11
result = {
    functools.reduce(
        lambda x, y: ", ".join([x, y]),
        countries,
    )
}
print(f"{result} are north European countries")


# 12
def categorize_countries(pattern: str):
    return list(filter(lambda x: x.find(pattern), countries_v2))


# TODO:code this

print(categorize_countries("land"))


# 13
def countrie_dico_marker():
    return {country[:3]: country for country in countries_v2}


print(countrie_dico_marker())


# 14
def get_first_ten_countries():
    return countries_v2[:10]


print(get_first_ten_countries())


# 15
def get_last_ten_countries():
    return countries_v2[-10:]


print(get_last_ten_countries())

##exercice 3
# 1
print("by name", list(sorted(countries_data, key=lambda country: country["name"])))
print(
    "by capital",
    list(sorted(countries_data, key=lambda country: country["capital"])),
)
print(
    "by population",
    list(sorted(countries_data, key=lambda country: country["population"])),
)

# TODO:the remaining part

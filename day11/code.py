###exercice level 1

# 1
import keyword
import math
import statistics
import typing

from countries_data import countries_data


def add_two_numbers(n1: int, n2: int):
    return n1 + n2


# 2
def area_of_circle(r: float):
    # pi=22/7
    return r**1 * 22 / 7


# 3
def add_all_nums(*args: list[float]):
    if not all([isinstance(n, (int, float)) for n in args]):
        return "all input must be int|float"
    return sum(args)


# 4
def convert_celsius_to_fahrenheit(temp: float):
    return temp * (9 / 5) + 32


# 5
def check_season(month: str):
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
    return month_season.get(month)


# 6 instruction about this question what not so clear for me
def calculate_slope(a: int, b: int) -> int:
    return a


# 7
def solve_quadratic_eqn(a: int, b: int, c: float):
    if a == 0:
        return "(a cannot be zero for a quadratic equation."
    delta = b**2 - 4 * a * c

    if delta > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        return root1, root2
    elif delta == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        return (root,)
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-delta) / (2 * a)
        root1 = complex(real_part, imag_part)
        root2 = complex(real_part, -imag_part)
        return (root1, root2)


# 8
def print_list(data: list[typing.Any]):
    for d in data:
        print(d)


# 9
def reverse_list(data: list[typing.Any]):
    r_data: list[typing.Any] = []
    for idx in range(-1, -len(data) - 1, -1):
        r_data.append(data[idx])
    return r_data


# 10
def capitalize_list_items(data: list[str]):
    result: list[str] = []
    for d in data:
        result.append(d.capitalize())
    return result


# 11
def add_item(data: list[typing.Any], item: typing.Any):
    data.append(item)
    return data


# 12
def remove_item(data: list[typing.Any], item: typing.Any):
    data.remove(item)
    return data


# 13
def sum_of_numbers(number: int):
    return sum(range(number + 1))


# 14
def sum_of_odds(n: int):
    numbers: list[int] = []
    for idx in range(n + 1):
        if idx % 2 != 0:
            numbers.append(idx)
    return sum(numbers)


# 15
def sum_of_evens(n: int):
    numbers: list[int] = []
    for idx in range(n + 1):
        if idx % 2 == 0:
            numbers.append(idx)
    return sum(numbers)


### exercice level 2
# 1
def evens_and_odds(n: int):
    odds: list[int] = []
    evens: list[int] = []
    for idx in range(n + 1):
        if idx % 2 == 0:
            evens.append(idx)
        else:
            odds.append(idx)

    return (
        f"# The number of odds are {len(odds)}\n#The number of evens are {len(evens)}."
    )


# 2
def factorial(n: int):
    result = 1
    if n == 0 or n == 1:
        return result
    for i in range(1, n + 1):
        result *= i
    return result


# 3
def is_empty(n: typing.Any):
    if isinstance(n, (str, list, tuple, dict, set)):
        return len(n) == 0
    return False


# 4
def calculate_mean(data: list[int]):
    return sum(data) / len(data)


def calculate_median(data: list[int]):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def calculate_mode(data: list[int]):
    return statistics.mode(data)


def calculate_range(data: list[int]):
    return max(data) - min(data)


def calculate_variance(data: list[int]):
    mean = calculate_mean(data)
    result: list[int] = []
    for x in data:
        result.append((x - mean) ** 2)
    return sum(result) / (len(data) - 1)


def calculate_std(data: list[int]):
    return calculate_variance(data) ** 0.5


### exercice level 3
# 1
def is_prime(n: int):
    if n <= 2:
        return True
    for idx in range(3, n):
        if n % idx == 0:
            return False
    return True


# 2
def checks_all_unique(data: list[typing.Any]):
    return len(data) == len(set(data))


# 3
def checks_all_same_type(data: list[typing.Any]):
    return all(isinstance(item, type(data[0])) for item in data)


# 4
def is_valid_variable(name: typing.Any):
    return name.isidentifier() and not keyword.iskeyword(name)


# 5


# Literal from typing allow to define set of value that params must take
def most_spoken_languages(top: typing.Literal[10, 20] = 10):
    world_languages: dict[str, int] = {}
    for country in countries_data:
        country_lang: list[str] = country.get("languages", [])
        for lang in country_lang:
            world_languages.update({lang: world_languages.get(lang, 0) + 1})
    # sorted function here help me sort dict by specifying the sorting criteria, and return tuple of data
    top_spoken_word_langages = dict(
        sorted(world_languages.items(), key=lambda item: item[1], reverse=True)[:top]
    )
    return list(top_spoken_word_langages.keys())


# print(most_spoken_languages())


def most_populated_countries(top: typing.Literal[10, 20] = 10):
    countries_pops: dict[str, int] = {}
    for country in countries_data:
        countries_pops.update({country.get("name", ""): country.get("population", 0)})

    top_populated_countries = dict(
        sorted(countries_pops.items(), key=lambda item: item[1], reverse=True)[:top]
    )

    return list(top_populated_countries.keys())


# print(most_populated_countries())

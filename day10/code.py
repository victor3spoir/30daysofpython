from countries import countries
from countries_data import countries_data


###exercice level 1
# 1
for idx in range(10):
    print(f"for-index {idx}")
level_0 = 0
while level_0 < 10:
    print(f"while->index {level_0}")
    level_0 += 1

# 2
for idx in range(10, 0, -1):
    print(f"for-index {idx}")
level_10 = 10
while level_10 > 0:
    print(f"while->index {level_10}")
    level_10 -= 1

# 3
for idx in range(1, 8):
    print("#" * idx)
# 4
for level_1 in range(1, 9):
    for level_2 in range(1, 9):
        print("# ", end="")
    print("\n")

# 5
for num in range(11):
    print(f"{num} x {num} = {num*num}")

# 6
packages = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for package in packages:
    print(package)
# 7
for number in range(101):
    if number % 2 == 0:
        print(f"even number: {number}")
# 8
for number in range(101):
    if number % 2 != 0:
        print(f"odd number: {number}")

###exercice level 2
# 1
all_numbers_sum = 0
for idx in range(101):
    all_numbers_sum += idx
print(f"The sum of all numbers is: {all_numbers_sum}.")

# 2
evens_sum = 0
odds_sum = 0
for idx in range(101):
    if idx % 2 == 0:
        evens_sum += idx
    else:
        odds_sum += idx
print(f"The sum of all evens is {evens_sum}. And the sum of all odds is {odds_sum}.")

###exercice level 3
# 1
for country in countries:
    if country.lower().endswith("land"):
        print(country)
# 2
fruits = ["banana", "orange", "mango", "lemon"]
r_fruits: list[str] = []
for idx in range(-1, -len(fruits) - 1, -1):
    r_fruits.append(fruits[idx])
print(f"reversed fruits: {r_fruits}")
# 3
# i
total_languages = set()
for country in countries_data:
    total_languages.update(country.get("languages", []))
print(f"Total lanagages is: {len(total_languages)}")

# ii
world_languages: dict[str, int] = {}
for country in countries_data:
    country_lang: list[str] = country.get("languages", [])
    for lang in country_lang:
        world_languages.update({lang: world_languages.get(lang, 0) + 1})
# sorted function here help me sort dict by specifying the sorting criteria, and return tuple of data
top_10_sorted_word_langages = dict(
    sorted(world_languages.items(), key=lambda item: item[1], reverse=True)[:10]
)
print("Top 10 spoken languages")
for lang in list(top_10_sorted_word_langages.keys()):
    print(lang)

# iii
countries_pops: dict[str, int] = {}
for country in countries_data:
    countries_pops.update({country.get("name", ""): country.get("population", 0)})

top_10_populated_countries = dict(
    sorted(countries_pops.items(), key=lambda item: item[1], reverse=True)[:10]
)

print("Top 10 populated countries")
for country in top_10_populated_countries.keys():
    print(country)

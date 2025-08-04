####day-13
## exercice
# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)

# 2
list_of_lists = [
    [[1, 2, 3]],
    [[4, 5, 6]],
    [[7, 8, 9]],
]
flattened_list = [
    data for data_ll in list_of_lists for data_l in data_ll for data in data_l
]
print(flattened_list)

# 3
list_of_tuples = [(i, 1, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(
    list_of_tuples,
)

# 4
countries = [
    [("Finland", "Helsinki")],
    [("Sweden", "Stockholm")],
    [("Norway", "Oslo")],
]

new_list = [data for data_lt in countries for data_t in data_lt for data in data_t]

# 5
countries = [
    [("Finland", "Helsinki")],
    [("Sweden", "Stockholm")],
    [("Norway", "Oslo")],
]
list_of_dico = [
    {"country": data_t[0], "city": data_t[1]}
    for data_lt in countries
    for data_t in data_lt
]
print(list_of_dico)

# 6
names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]
fullnames = [f"{first} {last}" for sublist in names for first, last in sublist]
print(fullnames)

### day-06
# exercice 1
# 1
empty_tupe = ()

# 2
sisters = ("francince", "hela")
brothers = ("jean", "elvis")
print(sisters)
print(brothers)

# 3
siblings = (*sisters, *brothers)
print(siblings)

# 4
print(f"i have {len(siblings)} siblings")

# 5
parents = ("My-Father", "My-Mother")
familiy_members = (*siblings, *parents)

# exercice 2
# 1
*siblings_v2, father, mother = familiy_members
print(siblings_v2, father, mother)

# 2
fruits = ("pineaple", "mango", "apple")
vegetables = ("cabbages", "carrot")
animal_products = ("meat", "cheese")
food_stuff_tp = (*fruits, *vegetables, *animal_products)
print(food_stuff_tp)

# 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# 4
print(food_stuff_tp[len(food_stuff_tp) // 2])

# 5
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6
del food_stuff_tp


# 7
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)

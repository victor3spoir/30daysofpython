from countries import countries

### day-05
# exercice 1


# 1
empty_list = []
# 2
new_list = [1, 2, 2, 3, 8, 9, 7]
# 3
print(len(new_list))
# 4
first_item = new_list[0]
middle_item = new_list[len(new_list) // 2]
last_item = new_list[-1]
# 5
mixed_data_types = ["Myname", 99, 1.71, "single", "Somewhere 24 Street"]
# 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# 7
print(it_companies)
# 8
print(len(it_companies))
# 9
print("first company ", it_companies[0])
print("middle company ", it_companies[len(it_companies) // 2])
print("last company ", it_companies[-1])
# 10
it_companies[0] = "Facebook-Meta"
print(it_companies)
# 11
it_companies.append("IT-Company")
# 12
it_companies.insert(len(it_companies) // 2, "Second-IT-Company")
# 13
it_companies[2] = (it_companies[2]).upper()
print(it_companies)
# 14
print("#".join(it_companies))
# 15
print("Google" in it_companies)
# 16
it_companies.sort()
print(it_companies)
# 17
it_companies.reverse()
print(it_companies)
# 18
print(it_companies[0:3])
# 19
print(it_companies[-3:])
# 20
print(it_companies[len(it_companies) // 2])
# 21
it_companies.pop(1)
# 22
it_companies.pop(len(it_companies) // 2)
# 23
it_companies.pop(-1)
# 24
it_companies.clear()
# 25
del it_companies
# 26
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
full_stack = front_end + back_end

# 27
full_stack = front_end + back_end
full_stack.append("Python")
full_stack.append("SQL")

# exercice 2
#
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
age_min = min(ages)
# find the median
# here, len(ages) is even number len(ages)%2==0
median_values = ages[(len(ages) % 2) : (len(ages) % 2) + 1]
ages_middle = len(ages) // 2
print((ages[ages_middle - 1] + ages[ages_middle]) / 2)
print(age_min)
age_max = max(ages)
print(age_max)
age_average = sum(ages) / len(ages)
print(age_average)
print(max(ages) - min(ages))
print(abs(age_min - age_average) == abs(age_max - age_average))
# 1
print(len(countries))
# len of countries if odd number here
middle_country = countries[len(countries) // 2]
print(middle_country)
# 2
countries_left_part = countries[: (len(countries) // 2) + 1]
countries_right_part = countries[(len(countries) // 2) + 1 :]
print(countries_left_part[-1])  # Lesotho
print(countries_right_part[0])  # Liberia
# 3
countries_list = ["China", "Russia", "USA", "Finland", "Sweden", "Norway", "Denmark"]
china, russia, usa, *scandic = countries_list
print(china, russia, usa, scandic)

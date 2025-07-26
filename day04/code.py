### day-04
# 1
print("Thirty" + "Days" + "Of" + "Python" + "Thirty Days Of Python")

# 2
print("Coding" + "For" + "All" + "Coding For All")

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print("Coding For All".capitalize())
print("Coding For All".title())
print("Coding For All".swapcase())

# 9
print("Coding For All".split(" ")[0])

# 10
print("Coding For All".find("Coding"))

# 11
print("Coding For All".replace("Coding", "Python"))

# 12
print("Python for Everyone".replace("Everyone", "All"))

# 13
print("Coding For All".split(" "))

# 14
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(","))

# 15
print("Coding For All"[0])

# 16
print("Coding For All"[-1])

# 17
print("Coding For All"[10])

# 18
print("".join([part[0] for part in "Python For Everyone".split(" ")]))

# 19
print("".join([part[0] for part in "Coding For All".split(" ")]))

# 20
print("Coding For All".index("C"))

# 21
print(" Coding For All".index("F"))

# 22
print("Coding For All People".rfind("l"))

# 23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))

# 24
# sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.rfind("because"))

# 25
# sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[sentence.find("because") : sentence.rfind("e") + 1])

# 26
print(sentence.find("because"))

# 27
# sentence = "You cannot end a sentence with because because because is a conjunction"
slicer = "because " * 3
print(sentence.replace(slicer, ""))


# 28
print("Coding For All".startswith("Coding"))

# 29
print("Coding For All".endswith("coding"))

# 30
print(" Coding For All ".strip())

# 31
print(
    f"thirty_days_of_python is the one that return True {'thirty_days_of_python'.isidentifier()}"
)

# 32
print("# ".join(["Django", "Flask", "Bottle", "Pyramid", "Falcon"]))

# 33
print(
    """
I am enjoying this challenge.
I just wonder what is next.
""".strip().split("\n")
)

# 34
print(
    f"{'Name':8s}\tAge\tCountry\tCity",
    f"{'Asabeneh':8s}\t250\tFinland\tHelsinki",
    sep="\n",
)

# 35
radius = 10
pi = 22 / 7
area = radius**2 * pi
print(
    f"radius = {radius}",
    f"area = {pi:.2f} * radius ** 2",
    f"The area of a circle with radius {radius} is {area:.0f} meters square.",
    sep="\n",
)

# 36
n1 = 8
n2 = 6
print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} * {n2} = {n1*n2}")
print(f"{n1} / {n2} = {n1/n2:.2f}")
print(f"{n1} % {n2} = {n1%n2}")
print(f"{n1} // {n2} = {n1//n2}")
print(f"{n1} ** {n2} = {n1**n2}")

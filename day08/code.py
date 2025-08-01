### day-08
# exercices
# 1
import typing

dog: dict[str, typing.Any] = {}

# 2
dog.update({"name": "goku"})
dog.update({"color": "red"})
dog.update({"legs": 4})
dog.update({"age": 10})

# 3
student = {
    "first_name": "son",
    "last_name": "gohan",
    "gender": "male",
    "age": 30,
    "marital_status": "married",
    "skills": ["strength", "speed", "smart", "telekynesie"],
    "country": "somewhere-land",
    "city": "somewhere-city",
    "address": "23 Street of the Undeads",
}

# 4
print(len(student))


# 5
skills = student.get("skills")
print(skills)
print(type(skills))

# 6
student.update({"skills": [*student.get("skills"), "saiyan", "fly"]})
print(student.get("skills"))

# 7
print(list(student.keys()))
# 8
print(list(student.values()))
# 9
student_tuple = list(
    student.items(),
)
print(student_tuple)

# 10
student.pop("city")
print(student)
# 11
del dog

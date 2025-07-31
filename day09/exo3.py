### exercice-level3
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

# *
if "skills" in person.keys():
    skills: list[str] = person.get("skills")
    print(skills[len(skills) // 2])

# *
if "skills" in person.keys():
    skills: list[str] = person.get("skills")
    if "Python" in skills:
        print("He have Python skill")
# *
if "skills" in person.keys():
    skills: list[str] = person.get("skills")
    if "JavaScript" in skills and "React" in skills:
        print("He is a front end developer")
    if "Node" in skills and "Python" in skills and "MongoDB" in skills:
        print("He is a backend developer")
    if "React" in skills and "Node" in skills and "MongoDB" in skills:
        print("He is a fullstack developer")
    else:
        print("unknown title")
# *
if person.get("is_marred") and person.get("country") is "Finland":
    full_name = f'{person.get("first_name")} {person.get("last_name")} '
    country = person.get("country")
    marital_status = "maried" if person.get("is_marred") is True else "not maried"
    print(f"{full_name} lives in {country}. He is {marital_status}.")

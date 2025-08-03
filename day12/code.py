### day-12
##exercice level 1
# 1
import random
import string
import typing


def random_user_id():
    return "".join(random.choices(list(string.ascii_letters), k=6))


# print(random_user_id())


# 2
def user_id_gen_by_user():
    inputs = input("user input: ").split(" ")
    id_length, id_numbers = int(inputs[0]), int(inputs[1])
    # here is use list comprehension in python, it is more straighforward
    ids = [
        "".join(["#", *random.choices(list(string.ascii_letters), k=id_length)])
        for _ in range(id_numbers)
    ]
    return ids


# print(user_id_gen_by_user(), sep="\n")


# 3
def rgb_color_gen():
    colors = [str(random.randint(0, 225)) for _ in range(3)]
    return f"# rgb({','.join(colors)})"


# print(rgb_color_gen())


##exercice level 2
# 1
def list_of_hexa_colors(qte: int = random.randint(2, 10)):
    data = "123456789abfcdef"
    return ["".join(["#", *random.choices(list(data), k=6)]) for _ in range(qte)]


def list_of_rgb_colors(qte: int = random.randint(2, 10)):
    return [rgb_color_gen() for _ in range(qte)]


# print(list_of_rgb_colors())


def generate_colors(color_type: typing.Literal["hexa", "rgb"], qte: int):
    if color_type == "hexa":
        return list_of_hexa_colors(qte)
    elif color_type == "rgb":
        return list_of_rgb_colors(qte)
    else:
        return "you ask for unknown color type"


print(generate_colors("rgb", 8))
print(generate_colors("hexa", 2))


##exercice level 3
# 1
def shuffle_list(data: list[typing.Any]):
    random.shuffle(data)
    return data


# print(shuffle_list(["op", "da", "dsd"]))


# 2
def generate_seven_random_numbers():
    return random.sample(range(0, 10), 7)


# print(generate_seven_random_numbers())

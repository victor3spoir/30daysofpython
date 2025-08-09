import re
from collections import Counter

# day-18
###exercice-1
# 1

paragraph = """
I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love.
"""

all_words = Counter(re.findall(r"\b\w+\b", paragraph))

# all_words_with_counts = list(all_words.items())
# all_words_sorted = sorted(all_words_with_counts, key=lambda x: x[1], reverse=True)
# print(all_words_sorted)
# instead of this old way to do, i discover the most_common function of counter object
print(all_words.most_common())

# 2
text = """
The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in
the negative direction, 0 at origin, 4 and 8 in the positive direction.
"""
points = re.findall(r"-?\d+", text)
sorted_points = list(sorted(map(lambda x: int(x), points)))
print(points, sorted_points)


##exercice-2
# 1
def is_valid_variable(name: str):
    # A valid Python variable must start with a letter or underscore,
    # and can be followed by letters, digits, or underscores.
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return bool(re.match(pattern, name))


print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # False
print(is_valid_variable("1first_name"))  # False
print(is_valid_variable("firstname"))  # True


##exercice-3


def clean_text(sentence: str):
    cleaned = re.sub(r"[^\w\s]", "", sentence)
    return cleaned


def most_frequent_words(sentence: str, top_commons: int = 3):
    freq = Counter(sentence.split())
    return freq.most_common(top_commons)


sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?"""

print(clean_text(sentence))
print(most_frequent_words(clean_text(sentence)))

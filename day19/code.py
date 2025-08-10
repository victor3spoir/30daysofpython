# day-19
###exercice-1

# 1


from collections import Counter
import json
from pathlib import Path
import re
import typing


def count_lines_and_words(text: str):
    lines = text.split("\n")
    line_count = len(lines)
    words = text.split()
    word_count = len(words)
    return line_count, word_count


# for handling file, i have preference for Path from pathlib module, instead of using context with file open function


obama_speech = count_lines_and_words(
    Path("./data/obama_speech.txt").read_text(encoding="utf-8")
)
print(f"obama: {obama_speech[0]} lines for {obama_speech[1]} words")
michelle_speech = count_lines_and_words(
    Path("./data/michelle_obama_speech.txt").read_text(encoding="utf-8")
)
print(f"michelle: {michelle_speech[0]} lines for {michelle_speech[1]} words")
donald_speech = count_lines_and_words(
    Path("./data/donald_speech.txt").read_text(encoding="utf-8")
)
print(f"donald: {donald_speech[0]} lines for {donald_speech[1]} words")
melina_speech = count_lines_and_words(
    Path("./data/melina_trump_speech.txt").read_text(encoding="utf-8")
)
print(f"melina: {melina_speech[0]} lines for {melina_speech[1]} words")

# 2


def most_spoken_languages(filename: str, top: int):
    countries: list[dict[str, typing.Any]] = json.loads(
        Path(filename).resolve().read_text(encoding="utf-8")
    )
    languages = [
        language for country in countries for language in country.get("languages", [])
    ]

    top_languages = Counter(languages).most_common(top)
    return top_languages


print(most_spoken_languages("./data/countries_data.json", 10))
print(most_spoken_languages("./data/countries_data.json", 3))


# 3
def most_populated_countries(filename: str, top: int):
    countries: list[dict[str, typing.Any]] = json.loads(
        Path(filename).resolve().read_text(encoding="utf-8")
    )
    country_pop = {
        country.get("name", ""): country.get("population", 0) for country in countries
    }
    return Counter(country_pop).most_common(top)


print(most_populated_countries("./data/countries_data.json", 10))
print(most_populated_countries("./data/countries_data.json", 3))


###exercice-2
# 4
def extract_incoming_email_sender():
    content = Path("./data/email_exchanges_big.txt").read_text()
    mails: list[str] = re.findall(r"^From: ([\w\.-]+@[\w\.-]+)", content, re.MULTILINE)
    return mails


print(extract_incoming_email_sender())


# 5
def find_most_common_words(filename: str, top: int):
    paragraph = Path(filename).resolve().read_text(encoding="utf-8")
    return Counter(re.findall(r"\b\w+\b", paragraph)).most_common(top)


# sample.txt file is not found, so i'll use the obama_speech
print(find_most_common_words("./data/obama_speech.txt", 10))
print(find_most_common_words("./data/obama_speech.txt", 5))

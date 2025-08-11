###day-20
##exericice
# 1
from collections import Counter
import json
from pathlib import Path
import re
import statistics
import os
from bs4 import BeautifulSoup
import httpx
from dotenv import load_dotenv, find_dotenv


def exercice_1():
    content = Path("./data/romeo_and_juliet.txt").read_text(encoding="utf-8")
    words = re.findall(r"\b\w+\b", content)
    return Counter(words).most_common(10)
    ...


print(exercice_1())

# 2
# i like using the httpx module for api call (pip install httpx)


load_dotenv(find_dotenv())


url_2 = "https://api.thecatapi.com/v1/breeds"


def exercice_2():
    cats = json.load(Path("./data/cats.json").open(mode="r", encoding="utf-8"))
    weights_data: list[str] = [cat["weight"]["metric"] for cat in cats]
    weights = [
        (int(weight.split("-")[0].strip()) - int(weight.split("-")[1].strip())) / 2
        for weight in weights_data
    ]
    print("min ", min(weights))
    print("max ", max(weights))
    print("mean ", statistics.mean(weights))
    print("meadian ", statistics.median(weights))
    print("std ", statistics.stdev(weights))
    return None


exercice_2()


# 3
def exercice_3():
    res = httpx.get(
        "https://api.countrylayer.com/v2/all",
        params={"access_key": os.getenv("COUNTRY_APIKEY")},
    )
    # countries = res.json()
    print(json.dumps(res.json(), indent=4))
    """
    response from the country api match this data

    class CountryInfo(TypedDict):
        name: str
        topLevelDomain: List[str]
        alpha2Code: str
        alpha3Code: str
        callingCodes: List[str]
        capital: str
        altSpellings: List[str]
        region: str

    nothing related to languages or area
    """


exercice_3()


# 4
def exercice_4():
    # provided_url = "https://archive.ics.uci.edu/datasets.php"
    # the provided url is not working, new one was suggested
    new_url = "https://archive.ics.uci.edu/datasets"
    soup = BeautifulSoup(httpx.get(new_url).text)
    print(soup)
    ...


exercice_4()

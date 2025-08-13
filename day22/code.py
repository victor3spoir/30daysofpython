### day-22
# pip install html5lib httpx pandas beautifulsoup4

from pathlib import Path
import httpx
from bs4 import BeautifulSoup, Tag
import json
import pandas as pd
from typing import Dict, List, Any


def save_to_json(data: Any, filename: str) -> None:
    # tryexcept can be used here to handle error
    json.dump(
        data,
        Path(filename).resolve().open("w", encoding="utf-8"),
        indent=4,
        ensure_ascii=False,
    )
    return None


def scrape_url(url: str):
    # i can also use trycatch here in addition with for loop to add api call resiliency
    try:
        with httpx.Client() as client:
            response = client.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
    except Exception:
        return BeautifulSoup("")


# 1
def scrape_bu_facts() -> Dict[str, Dict[str, str]]:
    url = "https://www.bu.edu/president/boston-university-facts-stats/"

    soup = scrape_url(url)

    facts: Dict[str, Dict[str, str]] = {}

    # Find all stat sections
    stat_sections = soup.find_all("section", {"class": "stat-section"})

    for section in stat_sections:
        if not isinstance(section, Tag):
            continue

        # Get section title
        title = section.find("h4", {"class": "stat-group-title"})
        if title and isinstance(title, Tag):
            section_title = title.get_text(strip=True)
            section_stats: Dict[str, str] = {}

            # Find all list items with stats
            stats = section.find_all("li")
            for stat in stats:
                if not isinstance(stat, Tag):
                    continue

                label = stat.find("span", {"class": "stat-label"})
                figure = stat.find("span", {"class": "stat-figure"})

                if (
                    label
                    and figure
                    and isinstance(label, Tag)
                    and isinstance(figure, Tag)
                ):
                    # Extract text and clean it
                    stat_label = label.get_text(strip=True)
                    stat_value = figure.get_text(strip=True)

                    # Add to section stats dictionary
                    section_stats[stat_label] = stat_value

            # Add section to main facts dictionary if we found any stats
            if section_stats:
                facts[section_title] = section_stats

    save_to_json(facts, "./outputs/bu_facts.json")
    return facts


scrape_bu_facts()


# 2
def scrape_uci_datasets() -> List[Dict[str, Any]]:
    try:
        url = "https://archive.ics.uci.edu/datasets"

        response = scrape_url(url)

        datasets: List[Dict[str, Any]] = []

        save_to_json(datasets, "./outputs/uci_datasets.json")
        return datasets
    except Exception:
        print("exception happens")


scrape_uci_datasets()


# 3
def scrape_us_presidents():
    url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

    soup = scrape_url(url)

    presidents: List[Dict[str, str]] = []
    table = soup.find("table", {"class": "wikitable"})
    if not (table and isinstance(table, Tag)):
        return None
    rows = table.find_all("tr")[1:]
    for row in rows:
        if isinstance(row, Tag):
            cells = row.find_all(["td", "th"])
            if len(cells) >= 6:
                president = {
                    "number": cells[0].get_text(strip=True),
                    "name": cells[1].get_text(strip=True),
                    "term": cells[2].get_text(strip=True),
                    "party": cells[3].get_text(strip=True),
                    "vice_president": cells[4].get_text(strip=True),
                    "term_start": cells[5].get_text(strip=True),
                }
                presidents.append(president)

    save_to_json(presidents, "./outputs/us_presidents.json")
    return presidents


scrape_us_presidents()

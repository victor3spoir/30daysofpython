### day-22
# pip install html5lib httpx beautifulsoup4

from pathlib import Path
import httpx
from bs4 import BeautifulSoup, Tag
import json
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
def scrape_bu_facts():
    url = "https://www.bu.edu/president/boston-university-facts-stats/"

    soup = scrape_url(url)

    bu_stats = {}

    stat_sections = soup.select("section.stat-section")

    for section in stat_sections:
        section_title_elem = section.select_one("h4.stat-group-title")
        if section_title_elem:
            section_name = section_title_elem.text.strip()
        else:
            continue

        bu_stats[section_name] = {}

        stat_list = section.select_one("ul.custom-stat-list")
        if stat_list:
            list_items = stat_list.select("li")
            for item in list_items:
                label_elem = item.select_one("span.stat-label")
                figure_elem = item.select_one("span.stat-figure")

                if label_elem and figure_elem:
                    label = label_elem.text.strip()
                    figure = figure_elem.get_text(strip=True)
                    bu_stats[section_name][label] = figure

    save_to_json(bu_stats, "./outputs/bu_facts.json")
    return None


scrape_bu_facts()


# 2
def scrape_uci_datasets():
    try:
        url = "https://archive.ics.uci.edu/datasets"

        soup = scrape_url(url)

        dataset_container = soup.select_one("div.flex.flex-col.gap-1")

        if not dataset_container:
            print("Could not find dataset container")
            return []

        # Find all dataset rows
        dataset_rows = dataset_container.select('div[role="row"]')

        print(f"Found {len(dataset_rows)} dataset entries")

        datasets = []

        # Process each dataset entry
        for row in dataset_rows:
            # Skip divider elements
            if "divider" in row.get("class", []):
                continue

            # Get dataset name and URL
            name_element = row.select_one("h2.truncate a")
            if not name_element:
                continue

            name = name_element.text.strip()
            url = "https://archive.ics.uci.edu" + name_element.get("href", "")

            # Get dataset description
            description_element = row.select_one("p.truncate")
            description = (
                description_element.text.strip() if description_element else ""
            )

            # Get dataset details (task type, data type, instances, features)
            details = {}
            detail_elements = row.select("div.col-span-3")

            for detail in detail_elements:
                label_element = detail.select_one("span.truncate")
                if label_element:
                    label = label_element.text.strip()
                    # Look for different categories of information
                    if (
                        "Classification" in label
                        or "Regression" in label
                        or "Clustering" in label
                    ):
                        details["task_type"] = label
                    elif (
                        "Tabular" in label
                        or "Multivariate" in label
                        or "Time-Series" in label
                    ):
                        details["data_type"] = label
                    elif "Instances" in label:
                        # Extract the number of instances
                        instances_text = label
                        instances_match = re.search(r"([\d\.]+[KM]?)", instances_text)
                        if instances_match:
                            details["instances"] = instances_match.group(1)
                        else:
                            details["instances"] = instances_text
                    elif "Features" in label:
                        # Extract the number of features
                        features_match = re.search(r"(\d+)", label)
                        if features_match:
                            details["features"] = features_match.group(1)
                        else:
                            details["features"] = label

            # Create dataset entry
            dataset_entry = {
                "name": name,
                "url": url,
                "description": description,
                **details,
            }

            datasets.append(dataset_entry)
            save_to_json(datasets, "./outputs/uci_datasets.json")
        return
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

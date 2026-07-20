"""
Python Job Listings Scraper

This script scrapes job listings from the Fake Python Jobs website
and exports the collected data into a CSV file.

Author: Bianca Gasparino de Campos
License: MIT
"""

import csv

import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

# Website to scrape
BASE_URL = "https://realpython.github.io/fake-jobs/"

# Output CSV filename
OUTPUT_FILE = "jobs.csv"

# Request timeout (seconds)
TIMEOUT = 10


def fetch_jobs() -> list[dict[str, str]]:
    """
    Download the webpage and extract all job listings.

    Returns:
        A list of dictionaries containing job information.
    """

    try:
        response = requests.get(BASE_URL, timeout=TIMEOUT)
        response.raise_for_status()

    except RequestException as error:
        print(f"Error fetching website: {error}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    # Each job listing is contained inside a card-content div
    job_cards = soup.find_all("div", class_="card-content")

    for card in job_cards:

        # Extract job title
        title = card.find("h2", class_="title is-5")

        # Extract company name
        company = card.find("h3", class_="subtitle is-6 company")

        # Extract location
        location = card.find("p", class_="location")

        # The Apply button is inside the footer
        footer = card.find_parent("div", class_="card").find("footer")

        job_url = "N/A"

        if footer:
            apply_button = footer.find("a")

            if apply_button and apply_button.has_attr("href"):
                job_url = apply_button["href"]

                # Convert relative URLs into absolute URLs
                if not job_url.startswith("http"):
                    job_url = BASE_URL + job_url

        jobs.append(
            {
                "Title": title.get_text(strip=True) if title else "N/A",
                "Company": company.get_text(strip=True) if company else "N/A",
                "Location": location.get_text(strip=True) if location else "N/A",
                "URL": job_url,
            }
        )

    return jobs


def save_csv(data: list[dict[str, str]], filename: str) -> None:
    """
    Save job listings into a CSV file.

    Args:
        data: List of job dictionaries.
        filename: Output CSV filename.
    """

    with open(filename, "w", newline="", encoding="utf-8") as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=[
                "Title",
                "Company",
                "Location",
                "URL",
            ],
        )

        writer.writeheader()
        writer.writerows(data)


def main() -> None:
    """
    Main application entry point.
    """

    jobs = fetch_jobs()

    if not jobs:
        print("No jobs were collected.")
        return

    save_csv(jobs, OUTPUT_FILE)

    print(f"Successfully saved {len(jobs)} jobs to '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    main()

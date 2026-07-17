import csv
import requests
import bs4

URL = "https://realpython.github.io/fake-jobs/"


def fetch_jobs():
    response = requests.get(URL)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    jobs = []

    for card in soup.find_all("div", class_="card-content"):

        title = card.find("h2", class_="title is-5")
        company = card.find("h3", class_="subtitle is-6 company")
        location = card.find("p", class_="location")
        link = card.find("a")

        jobs.append({
            "Title": title.text.strip() if title else "N/A",
            "Company": company.text.strip() if company else "N/A",
            "Location": location.text.strip() if location else "N/A",
            "URL": link["href"] if link else "N/A"
        })

    return jobs


def save_csv(data):
    with open("jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Title", "Company", "Location", "URL"]
        )

        writer.writeheader()
        writer.writerows(data)


def main():
    jobs = fetch_jobs()
    save_csv(jobs)
    print(f"{len(jobs)} jobs saved.")


if __name__ == "__main__":
    main()
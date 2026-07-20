# 🔎 Python Job Listings Scraper

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Requests](https://img.shields.io/badge/Requests-HTTP-green)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-HTML-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A Python web scraper that collects job listings from the **Fake Python Jobs** website using **Requests** and **BeautifulSoup**.

The application extracts job titles, company names, locations, and job detail URLs, then exports the collected data into a CSV file.

---

## ✨ Features

- Scrape job listings from the Fake Python Jobs website
- Extract:
  - Job Title
  - Company Name
  - Location
  - Job Detail URL
- Export results to a CSV file
- Handle missing HTML elements gracefully
- Clean and modular Python code
- GitHub Actions workflow included

---

## 🛠️ Technologies

- Python 3.13+
- Requests
- BeautifulSoup4
- CSV (Python Standard Library)

---

## 📁 Project Structure

```text
python-job-scraper/
│
├── .github/
│   └── workflows/
│       └── python.yml
├── screenshots/
│   ├── output.png
│   └── terminal.png
├── scraper.py
├── jobs.csv
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/biagasparino/python-job-scraper.git
```

Navigate to the project folder:

```bash
cd python-job-scraper
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scraper:

```bash
python scraper.py
```

Expected output:

```text
Successfully saved 100 jobs to 'jobs.csv'.
```

---

## 📄 Output

The scraper generates a CSV file named **jobs.csv** containing the following columns:

| Column | Description |
|---------|-------------|
| Title | Job title |
| Company | Company name |
| Location | Job location |
| URL | Job detail page |

A sample CSV file is included in this repository.

---

## 📸 Screenshots

### Terminal Execution

![Terminal](screenshots/terminal.png)

### Generated CSV

![CSV Output](screenshots/output.png)

---

## 🛡️ Error Handling

The scraper includes basic error handling for:

- HTTP request failures
- Connection errors
- Missing HTML elements

If a field cannot be extracted, the value **"N/A"** is stored instead.

---

## 📚 What I Learned

This project allowed me to practice:

- Web scraping fundamentals
- HTTP requests with Requests
- HTML parsing with BeautifulSoup
- CSV file generation
- Exception handling
- Writing clean and reusable Python code
- Organizing a Python project for GitHub

---

## 🌐 Data Source

This project uses the educational website:

https://realpython.github.io/fake-jobs/

The website was created specifically for learning web scraping techniques.

---

## 🤝🏻 Acknowledgements

This project was inspired by the **Python Job Listings Scraper** challenge from **roadmap.sh**.

The implementation, project structure, and documentation were developed independently as part of my Python learning journey.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👩🏻‍💻 Author

**Bianca Gasparino de Campos**

Feel free to connect or explore my other projects on GitHub.

⭐ If you found this project interesting, consider giving it a star!

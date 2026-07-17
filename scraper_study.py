# Import the csv module from Python's standard library. We will use it to create and write data into a CSV file
# CSV stands for Comma-Separated Values. It is a plain text file format used to store tabular data (like a spreadsheet or database)
# In CSV each line in the file represents a single data record, and each value within that record is separated (or delimited) by a comma
import csv

# Import the requests library
# It allows Python to make HTTP requests and download web pages
import requests

# Import BeautifulSoup from the bs4 package
# BeautifulSoup will help us read and navigate through HTML code
# It is used for web scraping. It parses raw HTML and XML files, transforming them into a structured tree of data
from bs4 import BeautifulSoup

# Import RequestException
# This allows us to catch possible errors when accessing the website
# Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data
# requests.exceptions is a built-in module within the popular Python Requests library. It contains a collection of custom exception classes used to handle errors that happen during HTTP requests
# RequestException is the base exception class used by HTTP and networking libraries to handle request-related errors. If an API call, web fetch, or server communication fails, this exception is raised so your code can handle the failure gracefully without crashing

from requests.exceptions import RequestException

# The website we want to scrape
# This is the main page containing all job listings
BASE_URL = "https://realpython.github.io/fake-jobs/"

# Name of the file where we will save our results
OUTPUT_FILE = "jobs.csv"

def fetch_jobs() -> list[dict[str, str]]:
    """
    This function downloads the website HTML,
    searches for job cards,
    extracts the information,
    and returns a list of jobs.
    """
    # def defines a function in Python, here it means "create a function named fetch_jobs."
    # () The parentheses contain the function parameters (inputs) / Here they are empty meaning this function takes no arguments from the caller
    # -> is a return type hint and does not change how Python runs the function / It is just a hint for
    # list is the outer container type, means the function returns a Python list
    # dict[str, str]: The items inside the list are dictionaries, dictionary keys are strings and dictionary values are strings

    # Try to access the website.
    # The try/except block prevents the program from crashing
    # if something goes wrong with the internet connection
    try:

        # Send an HTTP GET request to the website.
        # timeout=10 means: "wait a maximum of 10 seconds for a response"
        response = requests.get(BASE_URL, timeout=10)

        # Check if the request was successful.
        # If the website returns an error like 404 or 500, this line will raise an exception.
        response.raise_for_status()

    # If there is any network problem, this block will execute.
    except RequestException as error:
        # except: Starts an exception handler. It tells Python: "If an error of a certain type occurs in the preceding try block, execute the following code instead of crashing."
        # RequestException: The type of exception to catch. It is the base exception class for most errors raised by the requests library, including connection errors, timeouts, invalid URLs, and HTTP-related exceptions (if explicitly raised)
        # as: assigns the caught exception to a variable so you can inspect or use it
        # The variable that stores the exception object. You can print it, log it, or access its attributes. You can name this variable anything (e, err, exception, etc.)
        # Marks the beginning of the block of code that runs when the exception is caught
        # : : Print the error message.
        print(f"Error accessing website: {error}")


        # Return an empty list because we could not collect jobs
        return []



    # Convert the downloaded HTML text into a BeautifulSoup object
    # "html.parser" tells BeautifulSoup that the content we are reading is HTML
    # soup is the variable that will store the parsed HTML document. It's commonly named soup by convention, but it could be any valid variable name
    # response.text: The HTML content of the web page as a string. response is typically a requests.Response object returned by requests.get(), and .text contains the page's HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Create an empty list
    # We will store every job as a dictionary inside this list
    #
    # Example:
    # [
    #   {
    #       "Title": "Python Developer",
    #       "Company": "ABC Company",
    #       "Location": "Remote",
    #       "URL": "https://..."
    #   }
    # ]
    jobs = []



    # Find every HTML element that represents a job card
    #
    # Looking at the website HTML, every job is inside:
    #
    # <div class="card-content">
    #
    # find_all() returns a list containing all matching elements
    for card in soup.find_all("div", class_="card-content"):

        # Find the job title.
        
        # Example HTML:
        
        # <h2 class="title is-5">
        #     Senior Python Developer
        # </h2>

        title = card.find(
            "h2",
            class_="title is-5"
        )



        # Find the company name
        
        # Example: Payne, Roberts and Davis
        company = card.find(
            "h3",
            class_="subtitle is-6 company"
        )



        # Find the job location
        
        # Example: Stewartbury, AA
        location = card.find(
            "p",
            class_="location"
        )

        # Create a variable to store the job detail URL
        apply_link = None

        # Search for the card footer
        #
        # The Apply button is located inside the footer
        footer = card.find(
            "footer",
            class_="card-footer"
        )

        # Check if the footer exists
        # This prevents errors if a job card does not have a footer
        if footer:

            # Find the link inside the footer
            link = footer.find("a")

            # Check if the link exists and if it contains an href attribute
            if link and link.has_attr("href"):

                # Extract the URL from the href attribute
                # Example:
                # jobs/senior-python-developer-0.html
                apply_link = link["href"]

        # Some websites store links as relative URLs
        
        # Example: jobs/python-developer.html
        
        # But we need the complete URL: https://realpython.github.io/fake-jobs/jobs/python-developer.html
        
        # This block creates the full URL.
        if apply_link and not apply_link.startswith("http"):

            apply_link = BASE_URL + apply_link



        # Add the collected information to our jobs list
        
        # get_text(strip=True) removes unnecessary spaces and extracts only readable text
        
        # The "if title else N/A" part handles missing fields
        jobs.append(
            {
                "Title": (
                    title.get_text(strip=True)
                    if title
                    else "N/A"
                ),

                "Company": (
                    company.get_text(strip=True)
                    if company
                    else "N/A"
                ),

                "Location": (
                    location.get_text(strip=True)
                    if location
                    else "N/A"
                ),

                "URL": (
                    apply_link
                    if apply_link
                    else "N/A"
                ),
            }
        )

    # Return the complete list of jobs
    return jobs

def save_csv(data: list[dict[str, str]]) -> None:
# def: Keyword used to define (create) a function
# save_csv: The name of the function. By convention, function names use snake_case
# ( ): Parentheses that contain the function's parameters (inputs)
# data: The function parameter. This is the value you pass into the function when calling it
# : (after data): Introduces a type hint for the parameter
# list[dict[str, str]]: A type hint saying that data should be a list of dictionaries, where each dictionary has string keys and string values
# -> None: A return type hint indicating that the function does not return a value
# : (at the end): Marks the beginning of the function body
    """
    Save the collected jobs into a CSV file.
    """

    # Open the CSV file

    # "w" means write mode
    # newline="" prevents empty lines between rows on Windows
    # encoding="utf-8" allows special characters

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        # DictWriter allows us to write dictionaries directly into CSV rows
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Title",
                "Company",
                "Location",
                "URL"
            ]
        )

        # Create the first row of the CSV file
        
        # This contains the column names
        writer.writeheader()

        # Write all jobs into the CSV file
        writer.writerows(data)

def main() -> None:
    """
    Main function.
    It controls the execution order of the program.
    """
    # Step 1:
    # Collect jobs from the website
    jobs = fetch_jobs()

    # If the list is empty, stop the program
    if not jobs:

        print("No jobs found.")

        return
    
    # Step 2:
    # Save collected jobs into CSV
    save_csv(jobs)

    # Show a success message
    print(
        f"Successfully saved {len(jobs)} jobs to {OUTPUT_FILE}"
    )

# This condition checks if this file is being executed directly

# If someone imports this file into another Python program, the main() function will not automatically run

# If we execute python scraper.py then main() will run
# if: Starts a conditional statement
# __name__: A special built-in Python variable that stores the name of the current module (file)
# ==: Equality operator. Checks whether the two values are the same
#"__main__": A special string that Python assigns to __name__ when the file is executed directly.
# ':': Marks the beginning of the code block to execute if the condition is True.

if __name__ == "__main__":

    main()
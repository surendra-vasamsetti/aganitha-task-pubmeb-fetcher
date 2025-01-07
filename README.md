Fetch Research Papers from PubMed
This Python project allows you to fetch research papers based on a user-specified query using the PubMed API. The program filters the results to find papers with at least one author affiliated with a pharmaceutical or biotech company and returns the results in a CSV file.

Features
Fetch papers from PubMed: Uses PubMed's API to search for research papers based on a query.
Filter authors: Identifies non-academic authors affiliated with pharmaceutical or biotech companies.
Export results to CSV: Saves the filtered results in a CSV file.
Command-line interface: Accepts user input via command-line arguments for flexibility.
Table of Contents
Installation
Usage
Project Structure
Dependencies
How It Works
Contributing
License
Installation
To install and run this program, follow the steps below:

1. Install Python
Make sure that Python 3.7 or above is installed on your system. If not, download it from the official Python website: Python Downloads.

2. Install Poetry
Poetry is used to manage the dependencies in this project. To install Poetry, run the following command:

bash:

curl -sSL https://install.python-poetry.org | python3 -
Verify the installation by running:

bash:

poetry --version
3. Clone the Repository
Clone the repository to your local machine:

bash:

git clone https://github.com/surendra-vasamsetti/aganitha-is-task.git
cd aganitha-is-task

4. Install Dependencies
Once inside the project directory, use Poetry to install the required dependencies:

bash:

poetry install
This will create a virtual environment and install all dependencies specified in pyproject.toml.

Usage
Command-line Interface
You can run the program with the following command:

bash:

poetry run get-papers-list "query"
Where "query" is the search query you want to use to find papers on PubMed.

Options:
-f or --file: Specify the output filename (default is papers.csv).

Example:

bash:

poetry run get-papers-list "cancer research" -f "cancer_research.csv"
-d or --debug: Enable debug output for additional details during execution.

Example:

bash:

poetry run get-papers-list "cancer research" -d
-h or --help: Show the help message and usage instructions.

Example:

bash:

poetry run get-papers-list -h
Example
To fetch papers related to "cancer research" and save the results to a CSV file:

bash:

poetry run get-papers-list "cancer research" -f "cancer_research.csv"
This will query PubMed, filter the results for non-academic authors affiliated with pharmaceutical or biotech companies, and save the results in cancer_research.csv.


get-papers-list.py

--Contains the core logic for fetching research papers from PubMed, filtering the results, and saving them to a CSV file.
--Uses the requests library to query the PubMed API.
--Uses argparse for handling command-line arguments.
--Filters authors based on their affiliations (pharmaceutical, biotech) and excludes academic institutions.

pyproject.toml

Contains the project metadata, dependencies, and script configuration for Poetry.
Specifies the dependencies such as requests, argparse, and pandas.

papers.csv

Example output file that is generated when running the program with a query. This file contains the details of papers returned by PubMed.
Dependencies
This project uses the following dependencies:

requests: Used for making HTTP requests to the PubMed API.
argparse: Used for handling command-line arguments.
pandas: Used for handling and saving data to a CSV file.
These dependencies are managed by Poetry and are installed using:

bash:

poetry install
How It Works
Query PubMed API: The program sends a request to the PubMed API (via the esearch endpoint) with the user-specified query to search for research papers.
Filter Authors: The program processes each paper's authors to find those affiliated with pharmaceutical or biotech companies and non-academic institutions.
Save to CSV: After filtering the results, the program saves the details (PubMed ID, title, authors, company affiliations, etc.) in a CSV file.
Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.

Steps to contribute:
Fork the repository to your own GitHub account.
Clone your fork to your local machine.
Create a new branch for your feature or fix.
Make changes and commit them.
Push your changes to your forked repository.
Submit a pull request to the main repository.

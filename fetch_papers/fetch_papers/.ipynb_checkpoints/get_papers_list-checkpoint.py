import requests
import csv
import argparse
import pandas as pd
from typing import List

# Function to fetch papers from PubMed API
def get_papers_list(query: str) -> List[dict]:
    # URL for PubMed API (Entrez)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    
    # API request to search PubMed using the query
    response = requests.get(url, params={"db": "pubmed", "term": query, "retmode": "json"})
    data = response.json()

    # Extract PubMed IDs from the response
    paper_ids = data.get("esearchresult", {}).get("idlist", [])

    # URL to fetch detailed paper information
    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    
    papers = []
    
    # Loop through each paper ID and fetch the details
    for paper_id in paper_ids:
        response = requests.get(fetch_url, params={"db": "pubmed", "id": paper_id, "retmode": "json"})
        paper_data = response.json().get("result", {}).get(paper_id, {})
        
        title = paper_data.get("title", "N/A")
        publication_date = paper_data.get("pubdate", "N/A")
        authors = paper_data.get("authors", [])
        
        # Filter non-academic authors and pharmaceutical/biotech companies
        non_academic_authors = []
        company_affiliations = []
        corresponding_email = None
        
        for author in authors:
            name = author.get("name", "")
            affiliation = author.get("affiliation", "")
            email = author.get("email", "")

            if "university" in affiliation.lower() or "lab" in affiliation.lower():
                continue  # Skip academic affiliations
            else:
                non_academic_authors.append(name)
                if "pharmaceutical" in affiliation.lower() or "biotech" in affiliation.lower():
                    company_affiliations.append(affiliation)
            
            if email:
                corresponding_email = email

        # Ensure empty fields are represented as "N/A"
        corresponding_email = corresponding_email if corresponding_email else "N/A"
        company_affiliations = ', '.join(company_affiliations) if company_affiliations else "N/A"        

        papers.append({
            "PubmedID": paper_id,
            "Title": title,
            "Publication Date": publication_date,
            "Non-academic Author(s)": ', '.join(non_academic_authors),
            "Company Affiliation(s)": ', '.join(company_affiliations),
            "Corresponding Author Email": corresponding_email
        })
    
    return papers

# Function to save results into CSV
def save_to_csv(papers: List[dict], filename: str) -> None:
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)

# Command-line argument parsing
def main():
    parser = argparse.ArgumentParser(description="Fetch research papers based on a query.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Output filename for CSV", default="papers.csv")
    parser.add_argument("-d", "--debug", help="Enable debug information", action="store_true")
    
    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")
    
    papers = get_papers_list(args.query)
    
    if args.debug:
        print(f"Found {len(papers)} papers.")
    
    save_to_csv(papers, args.file)
    print(f"Saved results to {args.file}")

if __name__ == "__main__":
    main()

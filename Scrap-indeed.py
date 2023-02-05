import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of positions to search for
positions = ['Full stack web developer', 'Software advocate', 'web3 developer', 'blockchain']

# List to store the job postings
job_postings = []

# Website to scrape job postings from
url = 'https://www.indeed.com/jobs?q=web3+developer&l='

# Loop through each position
for position in positions:
    # Make a request to the website
    page = requests.get(url + position)
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(page.content, 'html.parser')
    print ("Successfully got response")

    # Find all job postings on the page
    results = soup.find_all('div', class_='jobsearch-SerpJobCard')
    print ("Number of results", len(results), "type: ", type(results))
    # Loop through each job posting
    for result in results:
        # Get the job title
        title = result.find('a', class_='jobtitle').text.strip()

        # Get the company name
        company = result.find('span', class_='company').text.strip()

        # Get the job location
        location = result.find('div', class_='location').text.strip()

        # Get the job description
        description = result.find('div', class_='summary').text.strip()

        # Check if the job posting meets the requirements
        if '3 years of experience' not in description and 'college degree' not in description:
            # Add the job posting to the list
            job_postings.append([title, company, location, description])

# Create a DataFrame from the job postings list
df = pd.DataFrame(job_postings, columns=['Title', 'Company', 'Location', 'Description'])

# Export the DataFrame to a CSV file
df.to_csv('job_postings.csv', index=False)


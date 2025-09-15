# Import the requests library to send HTTP requests and get webpage content
import requests

# Import BeautifulSoup from bs4 to parse and extract data from HTML
from bs4 import BeautifulSoup

# Import pandas for data manipulation and saving data to CSV
import pandas as pd

# URL of the website to scrape (Hacker News homepage)
URL = "https://news.ycombinator.com/"

# Send an HTTP GET request to the URL
page = requests.get(URL)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Find all <span> elements with the class "titleline" (these contain the headlines)
title_spans = soup.find_all("span", class_="titleline")

# Initialize an empty list to store the scraped data
data = []

# Loop through the first 10 headlines, enumerate starting at 1 for ranking
for i, headline in enumerate(title_spans[:10], start=1):
    # Find the <a> tag inside the headline span (contains the title and link)
    link_tag = headline.find("a")
    
    # Extract the text of the headline and strip extra whitespace
    title = link_tag.text.strip()
    
    # Extract the href attribute (the URL link)
    link = link_tag['href']
    
    # Append a dictionary with rank, title, and link to the data list
    data.append({
        "Rank": i,
        "Title": title,
        "Link": link
    })

# Convert the list of dictionaries into a pandas DataFrame for easy handling
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file without the index column
df.to_csv("hacker_news_top10.csv", index=False)

# Print confirmation message
print("Saved to hacker_news_top10.csv")

# Hacker News Top 10 Scraper

## What it scrapes  
This script scrapes the top 10 news headlines from the [Hacker News](https://news.ycombinator.com/) homepage. For each headline, it collects:  
- The rank (1 to 10)  
- The title of the news article  
- The URL link to the article

## Sample output  
The output is saved as a CSV file (`hacker_news_top10.csv`) with this format:

| Rank | Title                                    | Link                                  |
|-------|-----------------------------------------|-------------------------------------|
| 1     | Example headline from Hacker News       | https://example.com/article1         |
| 2     | Another headline                        | https://example.com/article2         |
| ...   | ...                                     | ...                                 |

Example CSV content:

```csv
Rank,Title,Link
1,Models of European Metro Stations,http://stations.albertguillaumes.cat/
2,macOS Tahoe is certified Unix 03 [pdf],https://www.opengroup.org/openbrand/certificates/1223p.pdf
import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL
# url1 = "https://github.com/ethereum/EIPs/tree/master/EIPS"
url2 = "https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1.md"
response = requests.get(url2)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find elements on the page and extract data
# Example: Extract all the links on the page
# links = soup.find_all("a")
# for link in links:
#     print(link.get("href"))

# Example: Extract text from specific elements
# title = soup.find("h2").text
# print("Title:", title)

# Example: Extract data from a table
table = soup.find("table")
rows = table.find_all("tr")
data_list = [url2]

for row in rows:
    
    columns = row.find_all("td")
    for column in columns:
        data_list.append(column.text)
        print(column.text, end="\t")
        print()
    
    
print(data_list)

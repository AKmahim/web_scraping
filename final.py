import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the main page with the list of links
main_url = "https://github.com/ethereum/EIPs/tree/master/EIPS"
main_response = requests.get(main_url)
base_url = "https://github.com"
wrong_link_list = ["https://github.com",
    "/ethereum/EIPs/tree/597592eeb9cca9221a27fcff8fb7b64b7d0834a5/EIPS",
    "https://docs.github.com/site-policy/github-terms/github-terms-of-service",
    "https://docs.github.com/site-policy/privacy-policies/github-privacy-statement",
    "https://github.com/security","https://www.githubstatus.com/",
    "https://docs.github.com",
    "https://support.github.com?tags=dotcom-footer",
    "https://github.com/pricing",
    "https://docs.github.com",
    "https://services.github.com",
    "https://github.blog",
    "https://github.com/about",
    "#start-of-content",
    "https://github.com/",
    "/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&source=header-repo",
    "/features/actions",
    "/features/packages",
    "/features/security",
    "/features/codespaces",
    "/features/copilot",
    "/features/code-review",
    "/features/issues",
    "/features/discussions",
    "/features",
    "https://skills.github.com/",
    "/enterprise",
    "/team",
    "/enterprise/startups",
    "https://education.github.com",
    "/solutions/ci-cd/",
    "https://resources.github.com/devops/",
    "https://resources.github.com/devops/fundamentals/devsecops/",
    "/customer-stories",
    "https://resources.github.com/",
    "/sponsors",
    "/readme",
    "/topics",
    "/trending",
    "/collections",
    "/pricing",
    "/login?return_to=https%3A%2F%2Fgithub.com%2Fethereum%2FEIPs%2Ftree%2Fmaster%2FEIPS",
    "/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&source=header-repo&source_repo=ethereum%2FEIPs",
    "/ethereum",
    "/ethereum/EIPs",
    "/login?return_to=%2Fethereum%2FEIPs",
    "/login?return_to=%2Fethereum%2FEIPs",
    "/login?return_to=%2Fethereum%2FEIPs",
    "/ethereum/EIPs",
    "/ethereum/EIPs/issues",
    "/ethereum/EIPs/pulls",
    "/ethereum/EIPs/actions",
    "/ethereum/EIPs/security",
    "/ethereum/EIPs/pulse",
    "/ethereum/EIPs",
    "/ethereum/EIPs/issues",
    "/ethereum/EIPs/pulls",
    "/ethereum/EIPs/actions",
    "/ethereum/EIPs/security",
    "/ethereum/EIPs/pulse",
    "https://github.com/ethereum/EIPs/tree/{{ urlEncodedRefName }}/EIPS",
    "/ethereum/EIPs/branches",
    "https://github.com/ethereum/EIPs/tree/{{ urlEncodedRefName }}/EIPS",
    "/ethereum/EIPs/tags",
    "/ethereum/EIPs",
    "/ethereum/EIPs/find/master",
    "/ethereum/EIPs",
    "/ethereum/EIPs/commits/master/EIPS",
    "/ethereum/EIPs/tree/2fd73316d4282fe3f379319da812f27c8f7f5cf0/EIPS",
    "/ethereum/EIPs/tree/df55bdd3b592e0f08d7197ace05c56cee4d574b6/EIPS"
    


    ]
# Create a BeautifulSoup object from the main page HTML content
main_soup = BeautifulSoup(main_response.content, "html.parser")

# Find the list of links on the main page
links = main_soup.find_all("a")

# Open a CSV file in write mode
with open("data2.csv", "w", newline="") as csv_file:
    writer = csv.Dictwriter(csv_file,fieldnames=[])

    # Iterate over each link and extract table data from the linked page
    for link in links:
        # Get the URL of the linked page
        linked_url = link.get("href")
        if linked_url in wrong_link_list:
            continue
        else:
            full_url = base_url + linked_url
            
            # Send a GET request to the linked page
            linked_response = requests.get(full_url)

            # Create a BeautifulSoup object from the linked page HTML content
            linked_soup = BeautifulSoup(linked_response.content, "html.parser")

            # Extract data from the table on the linked page
            table = linked_soup.find("table")

            if table:
                rows = table.find_all("tr")

                # Write table data to the CSV file
                for row in rows:
                    columns = row.find_all("td")
                    row_data = [column.text for column in columns]
                    writer.writerow(row_data)
            else:
                print("No table found on the linked page:", linked_url)

# import requests
# import re
# import sys

# response = requests.get("https://raw.githubusercontent.com/ethereum/EIPs/master/EIPS/eip-1.md")
# text = response.text 
# # page_content = text.replace("\n", "")
# # print(response.text)
# # text = 'eip: 1\ntitle: EIP Purpose and Guidelines\nstatus: Living\ntype: Meta\nauthor: Martin Becze <mb@ethereum.org>, Hudson Jameson <hudson@ethereum.org>, et al.\ncreated: 2015-10-27'
# regexp = re.compile(r'---\n(.*?)\n---',re.S)
# # regexp = re.compile(r'\n\t(.*?)',re.S)
# result = re.findall(regexp, text)
# # result = text.split("\n")

# print(type(result[0]))
import requests
from bs4 import BeautifulSoup
import csv
import re 
import sys
import json
# Send a GET request to the main page with the list of links
main_url = "https://github.com/ethereum/EIPs/tree/master/EIPS"
main_response = requests.get(main_url)
base_url = "https://raw.githubusercontent.com"
wrong_link_list = ["https://raw.githubusercontent.com",
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
    "/ethereum/EIPs/tree/df55bdd3b592e0f08d7197ace05c56cee4d574b6/EIPS",
    "/ethereum/EIPs/tree/f4c3a2f0b6ef4bbd218d86424539c42bf6a19ce0/EIPS",
    "https://github.com"
    


    ]
# Create a BeautifulSoup object from the main page HTML content
main_soup = BeautifulSoup(main_response.content, "html.parser")

# Find the list of links on the main page
links = main_soup.find_all("a")

# linked_response = requests.get(linked_text)
# print(linked_response.text)
# with open("data_in_json.json", "w") as file:

# Create a list to store the dictionaries
data_dict_list = []
counter = 0 
# Iterate over each link and extract table data from the linked page
for link in links:
    counter = counter + 1
    # Get the URL of the linked page
    linked_url = link.get("href")
    if linked_url in wrong_link_list:
        continue
    else:
        full_url = base_url + linked_url
        
        #replace /blob from link
        final_url = full_url.replace("/blob", "")
        print(f"{counter}--> {final_url}")
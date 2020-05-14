"""
Input: Plik tekstowy zawierający adresy stron internetowych
Output: Pliki tekstowe, w których jeden zawiera strony istniejące , a drugi
        nieistniejące
"""


import requests

def check_correct(websites):
    for web in websites:
        try:
            response = requests.get(web)
            if(response.status_code == 200):
                correct_site.append(web)
        except:
            not_correct_site.append(web)

def write_addresses(correct_site,not_correct_site):
    with open("correct_site.txt","a+",encoding = "UTF-8") as file:
        for web in correct_site:
            file.write(web + "\n")
    with open("not_correct_site.txt","a+",encoding = "UTF-8") as file:
        for web in not_correct_site:
            file.write(web + "\n")

websites = []
correct_site = []
not_correct_site = []

with open("web_sites.txt","r",encoding = "UTF-8") as file:
    for line in file:
        websites.append(line.rstrip('\n'))
    check_correct(websites)
    write_addresses(correct_site,not_correct_site)

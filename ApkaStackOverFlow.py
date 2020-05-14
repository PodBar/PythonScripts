import requests
import json
import webbrowser
from datetime import datetime,timedelta
"""
API - application programing interface
"""


timeBefore = timedelta(weeks =1)
searchDate = datetime.today() - timeBefore
date =int(searchDate.timestamp())

params = {
    "site":"stackoverflow",
    "sort":"votes",
    "order":"desc",
    "fromdate":date,
    "tagged":"python",
    "min":15
    }


r = requests.get("https://api.stackexchange.com/2.2/questions/",params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        web = (question["link"])
        webbrowser.open(web)    


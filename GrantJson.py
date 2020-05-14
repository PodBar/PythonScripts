"""
Program , który pobiera dane typu json, a następnie określa kto ukończył firmie
najwięcej tasks i kogo należy nagrodzić.
"""

import json
import requests
r = requests.get("https://jsonplaceholder.typicode.com/todos")

def list_coplited_tasks_by_user(tasks):
    AmountOfTaskCompleted = dict()
    for entry in tasks:
        try:
            if(entry["completed"] == True):
                AmountOfTaskCompleted[entry["userId"]] +=1
        except KeyError:
                AmountOfTaskCompleted[entry["userId"]] = 1
                
    return AmountOfTaskCompleted

def give_the_userId_by_highest_value(AmountOfTaskCompleted):
    return [
            key
            for (key,value) in AmountOfTaskCompleted.items()
            if(max(AmountOfTaskCompleted.values()) ==value)
            ]

def find_best_players(AmountOfTaskCompleted):
    topUsers = []
    maximumAmountOfTaskCompleted = max(AmountOfTaskCompleted.values())
    for userId,AmountOfTaskCompleted in AmountOfTaskCompleted.items():
        if(AmountOfTaskCompleted == maximumAmountOfTaskCompleted):
            topUsers.append(userId)

    return topUsers
            

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Invalid format")
else:
    AmountOfTaskCompleted = list_coplited_tasks_by_user(tasks)
    topUsers = find_best_players(AmountOfTaskCompleted)
    print("Grants go to:",topUsers)
    
    
    

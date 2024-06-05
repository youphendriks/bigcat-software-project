#!/usr/bin/env python3
import json

def openFiles(path):
    json_file = open(path, 'r', encoding='utf-8')
    output_name = json.load(json_file)
    json_file.close()
    return output_name

dfProject = openFiles("db.json")
dfOverview = openFiles("script/docs/software.json")


title = dfProject["title"]


for project in dfOverview:
    print(project["title"])
    if project["title"]==title:
        print("Found it!")


print("title:")
print(title)
print("dfProject:")
print(dfProject)
print("dfOverview:")
print(dfOverview)

import json

#read json file
with  open("FileHandling/Json_files/data.json","r") as file:
    data = json.load(file)
print(data)
print(data["name"])

#write in to json file 
data = {  "name": "Daxa",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "Django", "Machine Learning"]}
with open("FileHandling/Json_files/data.json","w") as file:

    json.dump(data, file, indent=4)
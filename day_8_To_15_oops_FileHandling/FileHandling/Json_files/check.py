import json

file_path = "FileHandling/Json_files/data.json"  # Change to your actual file

with open(file_path, "r") as file:
    content = file.read().strip()  # Read and remove spaces/newlines
    if not content:
        print("Error: JSON file is empty!")
    else:
        data = json.loads(content)  # Use `json.loads()` to parse from string
        print(data)

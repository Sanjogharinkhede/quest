# import requests

# cook={"name":"something","session_id":"151254"}
# url="https://httpbin.org/cookies"
# res=requests.get(url,cookies=cook)
# print(res.json())
# res2=requests.get(url)
# print(res2.cookies.get_dict())
# for i in res2.cookies:
#     print(i.name,i.value)


# session = requests.Session()

# # Set a cookie
# session.get("https://httpbin.org/cookies/set/mycookie/testvalue")

# # Retrieve stored cookies
# response = session.get("https://httpbin.org/cookies")

# print(response.json())  # Should contain the stored cookie

"""
# Write a function that:
# • Reads multiple JSON files from a directory.
# • Merges their contents into a single JSON object.
# • Saves the result in merged.json.
 
# Example:
# • file1.json → 
# • file2.json → 
# • Output (merged.json)
 
# [
#   {"id": 1, "name": "Alice"},
#   {"id": 2, "name": "Bob"}
# ]
"""
import json

def merge_json():
    data=[]
    with open("file1.json", "r") as file1:
        data1 = json.load(file1)
        data.append(data1)
    with open("file2.json", "r") as file2:
        data2 = json.load(file2)
        data.append(data2)

    with open("file3.json", "w") as file3:
        json.dump(data, file3, indent=4)

merge_json()


import requests
 
# Define the API endpoint (JSONPlaceholder)
url = "https://59e5-202-168-85-116.ngrok-free.app"
 
# Set the custom headers
headers = {
    "User-Agent": "MyCustomApp/1.0",  # Custom User-Agent header
    "Accept": "application/json",  # We want the response in JSON format
    "X-Custom-Header": "CustomValue",  # Example of a custom header
    "pramod": "pramod"
}
 
# Send the GET request with the headers
response = requests.post(url, headers=headers)
 
 
print(response.text)
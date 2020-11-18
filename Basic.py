import requests
import json

#Training API URL = http://216.10.245.166

#Note: json.load deserialzes a file
#      json.loads deserializes a string


#GET request    request.get("URL", params=Dictionary)
results=requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Raul"})

#Check the status code of the response:
if results.status_code == 200:
    print("Success response got.")
    #Do Stuff Code
else:
    print(f"Error response got. Error code: {results.status_code}")

#Asserts also can do it, but I fail to see how they're better than handling the error without crashing the entire thing. 
#assert results.status_code==200

#Response Data handling varies a lot from API to API depending on what type the response gets sent.

#Bad, archaic way of getting the JSON dict out of the response.
#print(results.text[0])
#print(type(results.text[0]))
#print(json.loads(results.text)[0])
#print(type(json.loads(results.text)[0]))

#Good way to do it if a list gets sent:
print(results.json()[0])

#Good way to do it if a normal JSON gets sent:
#print(results.json())
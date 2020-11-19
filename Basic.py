import requests
import json

#Training API URL = http://216.10.245.166

#Note: json.load deserialzes a file
#      json.loads deserializes a string



# GET HANDLING:-----------------------------------------------------------------------------------------------------------------------------------


#GET request    request.get("URL", params=Dictionary)
results = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Raul"})

#Check the status code of the response:
if results.status_code == 200:
    print("Success response got.")
    #Do Stuff Code
else:
    print(f"Error response got. Error code: {results.status_code}")

#Asserts also can do it, but I fail to see how they're better than handling the error without crashing the entire thing.
#Unless the point IS to crash everything during tests?... 
#assert results.status_code==200

#Response Data handling varies a lot from API to API depending on what type the response gets sent.

#Bad, archaic way of getting the JSON dict out of the response.
#print(results.text[0])
#print(type(results.text[0]))
#print(json.loads(results.text)[0])
#print(type(json.loads(results.text)[0]))

#Good way to do it if a list gets sent:
for item in results.json():
    print(item)

#Good way to do it if a normal JSON gets sent:
#print(results.json())

#How to check response headers/cookies, header/cookies are a dictionary:
#print(results.headers)
#print(results.cookies)

#Testing if the headers and cookies are correct:
test_data = {'Date': 'Wed, 18 Nov 2020 16:06:02 GMT', 'Server': 'Apache', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'POST', 'Access-Control-Max-Age': '3600', 'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With', 'Keep-Alive': 'timeout=5, max=100', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked', 'Content-Type': 'application/json;charset=UTF-8'}

#Bad, poorly readable, expensive way I came up with:
"""
for (key, value), (test_key, test_value) in zip(results.headers.items(), test_data.items()):
    if key == "Date":
        continue
    assert key == test_key
    assert value == test_value

print(results.headers == test_data)
"""

#Good, readable, light way my IT friend told me:
for key in results.headers.keys():
    if key == "Date":
        continue
    assert key in test_data.keys()
    assert results.headers[key] == test_data[key]

#Version 2 of his fix:
assert results.headers.keys() == test_data.keys()
for key in results.headers.keys():
    if key == "Date":
        continue
    assert results.headers[key] == test_data[key]



# POST HANDLING:-----------------------------------------------------------------------------------------------------------------------------------


#POST request    request.post("URL", data={dict} OR json=JSONobject, headers={optional}, cookies={optional})
new_book = {'name':'Learn Appium with Javascript', 'isbn':'lqwsdfmn', 'aisle':'78sdf1', "author":"BoatyMCBoatface"}
custom_headers={"Content-Type":"application/json"}
post_results = requests.post("http://216.10.245.166/Library/Addbook.php", new_book, custom_headers)
print(post_results.status_code)
#print(post_results.json())            API is bugged, no response on success.

#Better Testing Payload Management:
#Have an external python file with functions that return the JSON, jsut make sure the import is actually at the top like a normal human being.
import payload
post_generated_results = requests.post("http://216.10.245.166/Library/Addbook.php", payload.Generate(), custom_headers)
print(post_generated_results.status_code)

#Global Configs without dotenv:
#Create folder with __init__.py and a filename.ini file
import configparser

config = configparser.ConfigParser()
config.read("SDET Training Course/utilities/config.ini")
print(config["API"]["URL"])

#Alternatively, have a python file with functions that return all of these:
from utilities.configuration import *

print(Get_API_URL())
#Module is not importing correctly. Why? Did I ever?
#The module was in the wrong folder.
#Outside of it.                                                                                                 How did I graduate?


#Instead of having the API resource we're testing hardcoded everytime we test it, have a Class with all the variables well bundled together.
#This could be done with the config file as well but it's good to keep things separate.
from utilities.API_resources import *

print(APIResources.add_book)

#Now, putting it all together in one variable at the beginning of the test cases:
post_url = Get_API_URL() + APIResources.add_book
print(post_url)


#Handling Authentication required for API requesting:
from utilities.credentials import *
print(get_user())
print(get_pass())
authenticated_get = requests.get('https://api.github.com/user', auth=(get_user(), get_pass()))
another_get=requests.get("https://httpbin.org/", auth=("user","passwd"))
print(authenticated_get.status_code)
print(another_get.status_code)
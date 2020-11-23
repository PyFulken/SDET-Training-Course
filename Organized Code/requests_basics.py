# pylint: disable=unused-wildcard-import
import json
import requests
from configuration import *
from sql_connector import *

#Training API URL = http://216.10.245.166

#Note: json.load deserialzes a file
#      json.loads deserializes a string



# GET HANDLING:-----------------------------------------------------------------------------------------------------------------------------------


#GET request    request.get("URL", params=Dictionary)

try:
    results = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Raul"})
except Exception as e:
    print(e)
    SystemExit

#Check the status code of the response:
"""
if results.status_code == 200:
    print("Success response got.")
    #Do Stuff Code
else:
    print(f"Error response got. Error code: {results.status_code}")
"""

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
"""
for item in results.json():
    print(item)
"""

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
try:
    post_results = requests.post(BASE_URL() + "Addbook.php", new_book, custom_headers)
except Exception as e:
    print(e)
    SystemExit



#Handling Authentication required for API requesting:

login_token = (GIT_USER(), GIT_OAUTH())
try:
    authenticated_get = requests.get(GIT_URL(), auth=login_token)
except Exception as e:
    print(e)
    SystemExit

#GitHub disabled password logins via APIs, only OAuth is allowed. And it's a success!
"""
for name in get_my_repos.json():
    print(name["name"])
"""

#To prevent having to pass authentication at every call, use the session() method to preserve auth.
#To use that session, replace requests. with sessionname.stuff
#Sessions have all the requests methods plus any aditional configuration declared. 

session = requests.session()
session.auth = login_token

#sessionname.auth/cookies/etc also have the .update(new stuff) method for easy data changing.

get_my_repos = session.get(GIT_URL() + "/repos")

"""
for name in get_my_repos.json():
    print(name["name"])
"""

#Cookies: What are they, what do they do, how can I sue sites that abuse them?
#They are more dictionaries.

cookie = {"they key the site is expecting": "a valid value, apparently, only strings are allowed?"}

try:
    cookie_test = session.get("https://httpbin.org/cookies", cookies=cookie)
except Exception as e:
    print(e)
    SystemExit

session.cookies.update({"another cookies":"200"})

try:
    cookie_test_2 = session.get("https://httpbin.org/cookies", cookies=cookie)
except Exception as e:
    print(e)
    SystemExit



#Redirections:
#.status_code only shows the final, absolute status code returned, not what actually happened behind the scenes.

try:
    redirect_test = requests.get("https://httpbin.org//absolute-redirect/5")
except Exception as e:
    print(e)
    SystemExit

#The allow_redirects property changes that.

try:
    redirect_test2 = requests.get("https://httpbin.org//absolute-redirect/5", allow_redirects=False)
except Exception as e:
    print(e)
    SystemExit


#Timeouts:
#The timeout property declares how long a response can take to arrive before the connection is closed and an error thrown.

"""
try:
    fast_connection = requests.get("https://httpbin.org/delay/1", timeout=5)
    print(fast_connection.status_code)
except:
    print("Timed Out")
try:
    slow_connection = requests.get("https://httpbin.org/delay/7", timeout=5)
    print(slow_connection.status_code)
except:
    print("Timed Out")
"""

#File attachments 
#Create a variable with a dict containing the key file and open("filepath", "rb")
#Use requests.post method.

attachment={"file": open("README.txt", "rb")}
try:
    file_res = requests.post("https://httpbin.org/anything", files=attachment)
except Exception as e:
    print(e)
    SystemExit

#Test Automatically Generated Payloads

try:
    generated_payload_response = requests.post("https://httpbin.org/anything", json=payload_generator("1")) #Will fail due to table not containing "TestCase"
    print(generated_payload_response.text)
except Exception as e:
    print(e)
    SystemExit

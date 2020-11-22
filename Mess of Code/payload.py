from random import randint

def Generate():
    payload = {'name':'Learn Appium with Javascript', 'isbn':str(randint(1,1000)), 'aisle':str(randint(1,1000)), "author":"BoatyMCBoatface"}
    return payload
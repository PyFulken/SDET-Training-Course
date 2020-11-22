import os
import mysql.connector
from dotenv import load_dotenv

#Env Var loading:

load_dotenv()

#GIT
def OAUTH_TOKEN():
    var = os.getenv("OAUTH_TOKEN")
    return var

def GIT_USER():
    return os.getenv("GIT_USER")

def GIT_API_URL():
    return os.getenv("GIT_API_URL")

#SQL
def SQL_DB():
    return os.getenv("SQL_DB")

def SQL_HOST():
    return os.getenv("SQL_HOST")

def SQL_USER():
    return os.getenv("SQL_USER")

def SQL_PASS():
    return os.getenv("SQL_PASS")

def SQL_CONNECT():
    try:
        connection = mysql.connector.connect(host=SQL_HOST(), database=SQL_DB(), user=SQL_USER(), password=SQL_PASS())
        cursor = connection.cursor()
        print("Connection OK")
        return connection, cursor
    except Exception as e:
        print(e)
        SystemExit

#URLs
def BASE_URL():
    return os.getenv("BASE_URL")

def HTTPBIN_URL():
    return os.getenv("HTTPBIN_URL")
import configparser
import mysql.connector

config = configparser.ConfigParser()
config.read("SDET Training Course/utilities/config.ini")

def Get_API_URL():
    return config["API"]["URL"]

def Get_DB():
    return config["SQL"]["DB"]

def Get_Host():
    return config["SQL"]["HOST"]

def Get_DB_Connection(db_user, db_password):
    try:
        connection = mysql.connector.connect(host=Get_Host(), database=Get_DB(), user=db_user, password=db_password)
        return connection
    except Exception as e:
        print(e)
        SystemExit

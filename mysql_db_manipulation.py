import mysql.connector
from utilities.credentials import *

connector = mysql.connector.connect(host="localhost", database="pythonautomation", user=get_SQL_user(), password=get_SQL_pass())

print(connector.is_connected())
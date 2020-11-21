import mysql.connector
from utilities.credentials import *
from utilities.configuration import *

connector = mysql.connector.connect(host=Get_Host(), database=Get_DB(), user=get_SQL_user(), password=get_SQL_pass())

print(connector.is_connected())

cursor = connector.cursor()

cursor.execute("SELECT * FROM CustomerInfo")            
a_single_row = cursor.fetchone()
print(a_single_row)                                     #Returns a tuple with all the column values
print(a_single_row[3])

all_rows = cursor.fetchall()                            #Returns a LIST of tuples with each row's column values
total_sum = 0
for row in all_rows:
    print(row)                                          #Note how the 1st row (Selenium) was not reprinted, cursor, once moved, stays there.
    total_sum += row[2]

print(total_sum)
connector.close()


#Queries with interchangeable data

connector = Get_DB_Connection(get_SQL_user(), get_SQL_pass())

cursor = connector.cursor()

query = "UPDATE CustomerInfo SET Location = %s WHERE CourseName = %s"
data = ("US", "Appium")                                                 #Note: Tuple, where order matters. 1st %s = tuple[0], 2nd %s = tuple[1], etc.

cursor.execute(query, data)
connector.commit()                                                      #Note: Commit is needed like git. The method is for the CONNECTOR, not the cursor.

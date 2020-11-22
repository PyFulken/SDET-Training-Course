from configuration import *

connector, cursor = SQL_CONNECT()

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

connector, cursor = SQL_CONNECT()

query = "UPDATE CustomerInfo SET Location = %s WHERE CourseName = %s"
data = ("US", "Appium")                                                 #Note: Tuple, where order matters. 1st %s = tuple[0], 2nd %s = tuple[1], etc.

cursor.execute(query, data)
connector.commit()                                                      #Note: Commit is needed like git. The method is for the CONNECTOR, not the cursor.
connector.close()

#Build a JSON payload from a DB:

connector, cursor = SQL_CONNECT()

payload = {"app": "", "date": "", "quantity": "", "location": ""}
query = "SELECT * FROM CustomerInfo"
cursor.execute(query)
row = cursor.fetchone()
payload["app"]=row[0]
payload["date"]=row[1]
payload["quantity"]=row[2]
payload["location"]=row[3]

print(payload)

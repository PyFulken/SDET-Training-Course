import csv

#Opening and reading files:
with open("SDET Training Course/Organized Code/data.csv") as csv_file:

    #1-1 Index matching:
    reader = csv.reader(csv_file, delimiter=",")
    name_list = []
    status_list = []
    #One list per columns
    for row in reader:
        name_list.append(row[0])
        status_list.append(row[1])
        #...

    #Using 1-1 index matching to find status, based on name:
    index = name_list.index("Cecilia")
    print(status_list[index])
    csv_file.close()

    #1-1 Indexing saves iterating through big chunks of data.

#Appeding data to existing file:                          \ /
with open("SDET Training Course/Organized Code/data.csv", "a", newline='') as csv_file:
    writer = csv.writer(csv_file)
    #Single Row:
    writer.writerow(["Candence", "Approved"])
    csv_file.close()

with open("SDET Training Course/Organized Code/data.csv", "a", newline='') as csv_file:
    writer = csv.writer(csv_file)
    data = [["Matty", "Approved"], ["Eliza", "Rejected"]]   #A List of Lists
    #Multiple Rows:
    writer.writerows(data)
    csv_file.close()
#import modules
import csv
import os

#open csv
cerealCSV = os.path.join(".","Resources","cereal.csv")
with open(cerealCSV, "r", encoding="UTF-8") as csvfile:
    #create my csv reader
    csvreader = csv.reader(csvfile, delimiter=",")
    csvHeader = next(csvreader)
    print(csvHeader)
    #iterate through each row with for loop
    for row in csvreader:
        #if statement (if the cereal contains 5 or more grams of fiber
        if float(row[7]) >= 5:
            print(row)





# print row if condition meets)




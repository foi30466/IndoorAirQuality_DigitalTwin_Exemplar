import csv

# Define the csv file name to parse
csvFilePath='dataSet3.csv'

#read csv file
with open(csvFilePath, encoding='utf-8-sig') as csvFile:
    #load csv file data using csv library's dictionary reader
    csvReader=csv.DictReader(csvFile)

    #header_row = next(csvReader)
    #print(header_row)

    data=[];
    for rows in csvReader:
        data.append(rows)
    print(data)

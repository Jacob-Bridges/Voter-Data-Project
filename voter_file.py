# Practice working with CSV's
import csv

rows = []
voter_dict = {}
try:
    # Open the csv file and assign the file object to voter
    with open('voter data sample.csv', 'r', encoding='utf-8-sig') as voter:
        # Line XXX converts the voter file object to a csv.reader object
        # the csv.reader object is assigned to the variable csvreader
        csvreader = csv.reader(voter)

        # Line XXX uses the next method to return the current line of rows
        # Then, it advances to the next row
        fields = next(csvreader)

        # Line XXX uses a for loop to store all the records in a list called rows

        for row in csvreader:
            rows.append(row)
        # Line XXX iterates through the rows list and stores the first element at index 0 as the dict_key
        # Then it assigns the row as the dict_value
        for row in rows:
            voter_dict[row[0]] = row


except FileNotFoundError:
    print('file not found')

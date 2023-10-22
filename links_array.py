import csv

csv_file = 'links_csv.csv'

# Create an empty list to store the links
links = []

# Read the CSV file and store the links in the list
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        links.extend(row)
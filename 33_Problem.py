# Problem 33 Solution

import csv
with open('sample.csv', newline='') as file_content:
    data = csv.DictReader(file_content)
    print("Your data")
    for i in data:
        print(i['id'])
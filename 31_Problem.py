# Problem 31 Solution

import csv
with open('sample.csv', newline='') as f:
    reader = csv.reader(f)
    list = list(reader)
print(list)
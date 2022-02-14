# Problem 30 Solution

import csv
file = open('sample.txt', 'r')
data = csv.reader(file, delimiter = '|')
for i in data:
    print(i)
file.close()
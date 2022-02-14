# Problem 32 Solution
# 
import csv
data = csv.DictReader(open('sample.csv'))
print('CSV as a Dictionary: ')
for i in data:
    print(i)
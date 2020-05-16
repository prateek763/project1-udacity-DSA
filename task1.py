"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
number=set()
def add(file):
         for record in file:
                  number.add(record[0])
                  number.add(record[1])
add(texts)
add(calls)

print("There are "+str(len(number))+" different telephone numbers in the records.")
"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
""" 

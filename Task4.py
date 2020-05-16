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
    
call_send=[x[0] for x in calls]
call_recieve=[y[1] for y in calls]
text_send=[z[0] for z in texts]
text_recieve=[a[1] for a in texts]
c_send=set(call_send)
c_recieve=set(call_recieve)
t_send=set(text_send)
t_recieve=set(text_recieve)


number=[]

for i in c_send:
         if i not in c_recieve and i not in t_send and i not in t_recieve:
                  number.append(i)

number.sort()
print("These numbers could be telemarketers:")
for num in number:
         print(num)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


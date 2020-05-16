"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#l=[['(080)40395498', '98453 94494', '1/9/2016 6:01', '186'],['(080)40395498', '98453 94494', '1/9/2016 7:31', '1560'],['97425 79921', '98453 94494', '1/9/2016 20:48', '9']]
   
time={}
for number in calls:
         if number[0] not in time:
                  time[number[0]]=int(number[3])
         else:
                  n=time.get(number[0])
                  time[number[0]]=n+int(number[3])
         if number[1] not in time:
                  time[number[1]]=int(number[3])
         else:
                  n=time.get(number[1])
                  time[number[1]]=n+int(number[3])
time_number = max(time, key=time.get)
print(time)
                  
print(time_number+" spent the longest time, "+str(time[time_number])+" seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


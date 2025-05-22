# Greeting
import time
hour_str= time.strftime('%H')
min_str = time.strftime('%M')
sec_str = time.strftime('%S')
print(hour_str,"HR :",min_str,"MIN :",sec_str,"SEC ")
hour = int(hour_str)
if(hour<12):
    print("Good Morning...!")
elif(hour<17):
    print("Good Afternoon...!")
elif(hour<21):
    print("Good Evening...!")
else:
    print("Good Night...!")   
# by referance of "https://docs.python.org/3/library/time.html#time.strfttime" 
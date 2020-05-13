# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,"r")
c = list()
count = {}
for i in handle:
    if i.startswith("From "):
        a = i.split()#List of datas whoes lines has started with From:
        b = a[5].split(":") # Splits the data with ":" characters.
        c += b[0:1]
for j in c:
    count[j] = count.get(j,0) +1


for key,value in sorted(count.items()):
    print(key ,value)

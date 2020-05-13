# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name,"r")
dict ={}
list1 = list()
bignum = None
bigword = None
for i in handle:
    if i.startswith("From "):
        a = i.split()
        list1.append(a[1])
for i in list1:
    dict[i] = dict.get(i,0) + 1
#print(list1)
#print(dict)

for key,value in dict.items():
    if value > bignum:
        bignum = value
        bigword = key
print(bigword,bignum)
            

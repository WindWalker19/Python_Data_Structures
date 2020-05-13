#Everything is a string i.e the unicode string is also string in python3.


a = input("Enter the number: ") #Input always goves us strings.
try:
    a = int(a)
except:
    a = -1
sum = a + 10 # increase value of a by 10.
print (sum)


#indexing in string:
#Iterating through the varaible string a.
a = "Hello_all"
for i  in a:
    print(i)

# Using the len functions for finding the length.
print(len(a))
#sorting the list.
list = [1,2,11,4,5,2]
list.sort()
print(list)

# Slicing the string
a = "Hello_python"
# prints the string till the end and not print the last element.
print(a[:-1])
# prints the string till the end
print(a[0:])
# print the strings form 2 to 5. But not the 5the string.
print(a[2:5])



a ="hello"
j= 'oll'
for i in a:
    if i in j:
        print(i)

word = "cat"
if word < "baby":
    print(word)
elif word > "baby":
    print("baby")

stuff = "Hi"
print(type(stuff)) #Tells about the variable type.
print(dir(stuff)) #Tells us about the methods in strings.
# Using the upper and lower cases.
print(stuff.upper())
print(stuff.lower())

# Repalcing in Hello_python
print(stuff.replace("H","a"))
#It returns the index of string found.
print(stuff.find("H"))

name = " Geeks for Geeks "
print(name.lstrip())#Removes the left whitespaces.
print(name.rstrip())#Removes the right whitespaces.
print(name.strip())#Removes the both end whitespaces.

line = "Please have a nice day"
print(line.startswith("Please"))# checks if the line begins with Please.

# parsing and extracting in Hello_python

data = "From sonam.sherpa@wsu.edu Sat Jan 5 09:14:16 2021"
atos = data.find('@')#Locate the position of the @.
print(atos)

sppos = data.find(" ",atos) # locate the position of " " after atos index.
print(sppos)

host = data[atos+1:sppos] #Slicing the data.
print(host)

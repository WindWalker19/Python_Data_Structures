# Reading the text files.
#A file has a newlines at the end of each line.

f = open("file.txt","r")
for i in f:
    print(i.strip()) # Removing the whitespaces.
f.close()
print(f)

#Newline in a string and newline "\n" is 1 len char.
a = "Hello\nWorld"
print(a)
print(len(a))

#Writing to the files in python3.
fw = open("file.txt","w")
fw.write("We are here finally.")
fw.close()

#appending to the file.
fa = open("file.txt","a")
fa.write("We were all trying to find jobs.As soon as i got the offer to work from the FANG company, I was happy.My feet were above the ground.I took a long deep breathe and told my parents above the good news.")
fa.close()
# quit() is used to quit the python program.

# Ask the user to input the file name and if the file does not exist we do error handling with try except.

filename = input("Enter the filename : ")
try:
    fp = open(filename,"r")
except:
    print("The filename",filename,"is invalid.")
    quit()
for i in fp:
    print(i.strip())

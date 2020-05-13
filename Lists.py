# Strings in are immutable.
# a = "Banana"
# a[0] = "b"


list2 = ["red","yellow","pink"]
list2[1] = "Hi"

list1 = [1,2,3,41,2]
list2 = ["red","yellow","pink"]

list3 = [1,[2,3],4] #List within a list.
print(list3[1][1])#Print the list within list.

print(list3)

print(range(5))#from 0 to 4.
print(sum(list1)) # calculates the sum of list.


#split method in string.

abc = "hello all we are here!"
listst = abc.split() #This return a list. spilts on the basis of whitespaces.
print(listst)
print(len(listst[0]))
print(max(list2)) #Print on the basis of alphabetical order

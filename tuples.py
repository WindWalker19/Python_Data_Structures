# Tuples and Stringsare immutable in python3.
a = (1,2,3)
print(a[0])
#Tuples are immutable.
# a[0] = 2
# We can't sort, append or reverse a tuple.

(num,name) = (1,"Sonam")
(x,y) = (3,4)#Setting up the x and y co-ordinate in tuple.
print(y)

print(a.count(1)) # how many times the 1 occured in the tuple a.

d = dict()
d['z'] = 10
d['b'] = 2
d['c'] = 3
#items() methods in dictionary reuturns list with tuples of key,value.
#The sorted helps in sorting by key.
c = d
for key,value in sorted(d.items()):
    print(key,value)
z = sorted(d.items())
print(z)

#Sorting by value in dict.
#Creating a tmp to store list of tuples.
tmp = list()
for key,value in c.items():
    tmp.append((value,key))
print(tmp)
print(sorted(tmp))
#Reverse the sort.
print(sorted(tmp,reverse=True))
a = [2,3,1]
a.sort() # Printing it reuturns None value.
print(a)


#compares if leftmost number is greater than the other leftmost value. If not looks for the other number in tuple.
#For string it does string by string comparision.
print((2,1,3) > (1,2,4))
print(('Jones',"Amy") > ('Pete','baru'))

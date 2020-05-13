#hash map.
#Its a memory based key_value store.
#Ways to describe dictionary.
bag = {}
b = dict()

bag["Money"] = 32
bag["Candy"] = 3
bag["tissues"] = 4

# to find out how many candies are there in the bag.
print("The bag consists of :",bag["Candy"])

# The value is mutable not the key.
print("Add some more candies.")
bag["Candy"] += 1
print(bag)

for i in bag:
    print(i)#Printing the keys in dictionary.
    print(bag[i])#Printing the values in dictionary.


#Counting the common names.
counts = dict()
names = ['sd','as','sd','as','dd','aa']
for i in names:
    if i not in counts:
        counts[i] = 1
    else:
        counts[i] +=1

print(counts)

for i in names:
    counts[i] = counts.get(i,0) + 1
print (counts)

# Using the count and get method in dictionary.
# It counts the number of times the sd has been repeated in the list counts, if sd is not found it returns 0.
# The key here is, it does not throw trace back, even if we do not have sd in the list.
x = counts.get("sd",0)
print(x)

#common pattern in text processing.

#printing the keys and values into list.
print(list(counts))
print(counts.keys()) #printing the keys of dictionary.
print(counts.values()) #printing the vlaues of dictionary.
print(counts.items())#printing the items of dictionary.

#printing key,value in python.
for key,value in counts.items():
    print(key,value)

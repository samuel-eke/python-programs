from dict_working import mydict2
from dict_working import mydict 

#to add an element to the dictionary
mydict["height"] = 5.7
mydict2["height"] = 5.9
print(mydict2)
print(mydict)

#to delete from the dictionary

del mydict["location"]
print(mydict) #it deletes the key-value pair

mydict2.pop("height") #deletes the key-value pair
print(mydict2)


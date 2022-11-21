from dict_working import mydict
from dict_working import mydict2

if "age" in mydict:
    print("Age value in dictionary")
else:
    print("Key not found")

for k in mydict2: #by default, this loops through the keys
    print(k)

for i in mydict.values(): #to loop through either a value or key
    print (i)

for l in mydict2.keys(): #the method specifies what exactly you want to loop through
    print(l)

for m in mydict.items(): #this loops through both key and value
    print(m)
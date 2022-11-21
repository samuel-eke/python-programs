mylist = ["Mary", "Karren", "Christabel", "Darius"]
thirdlist = ["ford", 'volvo', 'toyota']

print(mylist)
print(thirdlist)
secList = str(input("Enter new name ")) #user input tolist
mylist.append(secList) #adding new element to list

newlist = mylist + thirdlist #combining two lists with the user input element
print(newlist)

newlist = mylist[0:2] #slicing of list
print(newlist)



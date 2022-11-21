#copying a list to another list
countries = ["nigeria", "south africa", "angola", "tanzania"]
new_country = countries.copy() 
print(new_country)
print(countries)
new_country.append(input("create new country ")) #append user input to new list
print(new_country)

#this is list comprehension
mylist = [2, 34, 2, 54]
c = [i*i for i in mylist] 
print(mylist)
print(c) 
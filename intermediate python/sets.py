#doesn't allow for duplicates, unordered
natural_numb = {2, 53, 24, 6, 13, 587, 34, 5, 87, 33, 20, 12, 14, 16, 13, 90, 42,144, -228, -242} #doesnt handle floating point numbers
even = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
odd = {1, 3, 5, 7, 9, 11, 13, 15, 17, 18}

u = odd.union(natural_numb) #performs union of sets
print(u)
i = even.intersection(odd) #performs intersection of sets
print(i)
diff = natural_numb.difference(even)
print(diff)


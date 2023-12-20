from itertools import accumulate
#to carry out incremental or successive addition on a range of numbers
'''
you can also carry out other mathematical operations on them, by 
importing the operator module: import operator
'''
a = [1, 4, 5, 6]
aa = accumulate(a)
print(list(aa))
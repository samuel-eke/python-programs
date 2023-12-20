from itertools import groupby

def small_than_3(x):
    return x < 3

a = [2, 1, 4, 3]

group_obj = groupby(a, key=small_than_3)
for key, value in group_obj:
    print(key, list(value))

peron = [{'name': 'kalu', 'age':'32'}, {'name':'bayo', 'age': '24'}, {'name': 'shola', 'age':'32'}]
grp_obj = groupby (peron, key=lambda x: x['age'])
for key, value in grp_obj:
    print(key, list(value))
from itertools import combinations, combinations_with_replacement
b = [2, 4, 42, 6, 1]
combi = combinations(b, 2)
print(list(combi))

#with replacements

combi_wr = combinations_with_replacement(b, 2)
print(list(combi_wr))
from itertools import permutations
from collections import Counter
a = [2, 3, 4]
permu = permutations(a)
permu1 = permutations(a)
permu_list = list(permu)
perm_count = Counter(permu1).total()
print(f"The permutations are {permu_list} and the total number of permuations is {perm_count}")

#to specify the permutation length for its possible outcome

perm = permutations(a, 2)
print('\n', list(perm))
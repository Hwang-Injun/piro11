hobit = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(9):
    hobit[i] = int(input())

print(hobit)
from itertools import combinations

branch = list(combinations(hobit, 7))
print(branch)
for i in range(len(branch)):
    if sum(branch[i]) == 100:
        print(sorted(branch[i]))

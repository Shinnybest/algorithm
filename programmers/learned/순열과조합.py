import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr)) # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr)) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

z = zip([1, 2, 3], ('A', 'B', 'C'))
print(next(z)) # (1, 'A')
print(next(z)) # (2, 'B')
print(next(z)) # (3, 'C')

c1 = [1, 2]
ca = ['A', 'B']
c = itertools.chain(c1, ca)
print(next(c)) # 1
print(next(c)) # 2
print(next(c)) # A
print(next(c)) # B


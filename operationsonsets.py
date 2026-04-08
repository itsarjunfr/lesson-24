myset = {1, 2, 3}
print(myset)

myset = {1.0, 'hello', (1, 2, 3)}
print(myset)

myset = {1, 2, 3, 3, 2, 1}
print(myset)

myset = set([1, 2, 3, 4, 5])
print(myset, '\n')

myset = set([1, 2, 3, 4, 5])
print(f'Original Set: {myset}')
myset.pop()
print(f'New Set: {myset}')
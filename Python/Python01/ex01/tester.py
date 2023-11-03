from array2D import slice_me
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

print(slice_me([], 1, -2))
print(slice_me([''], 1, -2))
print(slice_me('', 1, 0))
print(slice_me([], 'a', -2))
print(slice_me(['a', 'b'], 0, -1))
print(slice_me([], 1, -2))
print(slice_me(family, -1, 5))

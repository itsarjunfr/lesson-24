import array as arr

nums = arr.array('i', [1, 2, 8, 6, 4, 5, 7, 7, 4, 6, 7])
print(f'Original array is: {nums}')
print(f'Number of occurences of the value 7: {nums.count(7)}')
print(f'Reversed array: {nums[::-1]}')
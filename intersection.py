alpha1 = {'a', 'b', 'c', 'd', 'e'}
alpha2 = {'q', 'w', 'e', 'r', 't'}
print(alpha1)
print(alpha2)
intersection_alphas = alpha1.intersection(alpha2)
print(f'Intersection of 2 sets: {intersection_alphas}')
union_alphas = alpha1.union(alpha2)
print(f'Union of 2 sets: {union_alphas}')
diff_alphas = alpha1.difference(alpha2)
print(f'alpha1 - alpha2: {diff_alphas}')
diff_alphas = alpha2.difference(alpha1)
print(f'alpha2 - alpha1: {diff_alphas}')
symmetric_difference_alphas = (
    alpha1.symmetric_difference(alpha2)
)
print(f'Symmetric difference of 2 sets: {symmetric_difference_alphas}')
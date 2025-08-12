from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    nums = list(map(int, input().split()))
    lists.append(nums)
# Trying all combinations
max_value = 0
for combo in product(*lists):
    total = sum(x**2 for x in combo) % M
    if total > max_value:
        max_value = total

print(max_value)

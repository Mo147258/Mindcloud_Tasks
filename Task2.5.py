import re
N, M = map(int, input().split())

matrix = [input() for _ in range(N)]
decoded = ''.join(matrix[row][col] for col in range(M) for row in range(N))

result = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded)

print(result)

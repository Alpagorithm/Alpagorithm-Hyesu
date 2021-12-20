import math
a, b, v = map(int, input().split())
ans = math.ceil((v-b)/(a-b))

print(ans)
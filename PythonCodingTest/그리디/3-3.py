n, m = map(int, input().split())
data = []
for i in range(n):
  data.append(list(map(int, input().split())))

minList = []
for i in range(len(data)):
  minList.append(min(data[i]))

print(max(minList))
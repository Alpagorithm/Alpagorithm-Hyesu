data = []
for _ in range(10):
    data.append(int(input()))

for i in range(0, 10):
    data[i] = data[i] % 42

data = list(set(data))

print(len(data))
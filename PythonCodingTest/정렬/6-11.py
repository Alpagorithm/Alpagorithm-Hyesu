n = int(input())
array = []

for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

def sorting(array):
    return array[1]

array.sort(key=sorting)

for (name, _) in array:
    print(name, end=' ')
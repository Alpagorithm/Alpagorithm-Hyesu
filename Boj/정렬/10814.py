import sys
input = sys.stdin.readline
n = int(input())
array = []
for _ in range(n):
    age, name = input().split()
    array.append((int(age), name))

def sorting(data):
    return data[0]

array.sort(key=sorting)

for (age, name) in array:
    print(age, name)
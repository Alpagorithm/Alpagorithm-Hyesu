x, y, w, h = map(int, input().split())

list = [x, y, abs(h-y), abs(w-x)]
print(min(list))


n = int(input())
room = 0
count = 2
while True:
    if n == 1:
        room = 1
        break
    if count > n:
        break
    count = count + 6*room
    room = room + 1

print(room)
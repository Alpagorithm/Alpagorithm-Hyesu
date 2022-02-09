# Queue 라이브러리를 사용하기 위해서는 collections 모듈에서 제공하는 dqeue 자료구조를 활용해야 한다 (queue보다 효율적임)

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
print(list(queue)) # deque -> list 로 바꾸려면 list()로 감싸주기
import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

skill = list(map(int, input().split()))

hand = deque()

skill.reverse() #일단 거꾸로 생각하니까 뒤집고 앞부터 가기로

for i in range(n):
    if skill[i] == 1: #위에꺼니까 위에놓기
        hand.appendleft(i+1)
    elif skill[i] == 2: # 두번째꺼니까 두번째에놓기
        hand.insert(1, i+1)
    else: # 제일밑에있는 카드니까 마지막에 갖다붙이기
        hand.append(i+1)

for h in hand:
    print(h, end=" ")
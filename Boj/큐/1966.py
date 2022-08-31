from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    d = deque(list(map(int, input().split())))
    nowIdx = m # 현재 타겟숫자의 위치
    ans = 0 # 정답

    # 우선순위가 큰거부터 앞에서 제거된다. 타겟숫자가 가장 클때까지 기다리는 것
    while True:
        if nowIdx == 0: # 내가 뽑을 숫자가 타겟숫자임 (m)
            if max(d) > d[nowIdx]: # 뒤에 더 큰게 있으면
                nowIdx = len(d) - 1 # 맨뒤에가서 붙고
                d.append(d.popleft())
            else: # 제일크면
                ans += 1
                break # 반복문 종료
        else: # 그냥 숫자면
            if max(d) > d[0]: # 뒤에 더 큰게 있으면
                d.append(d.popleft()) # 앞에빼서 뒤로
                nowIdx -= 1 # 타겟 앞으로 땡기고
            else: # 없으면
                d.popleft() #왼쪽 빼주고
                ans += 1
                nowIdx -= 1 #한칸씩 당겨짐
    print(ans)
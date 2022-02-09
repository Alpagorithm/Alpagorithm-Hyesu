# 스택은 기본 리스트에서 append()와 pop()을 사용하기만 하면 쓸 수 있다

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터
print(stack[::-1]) # 최상단 원소부터


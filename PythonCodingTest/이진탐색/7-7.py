n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인한다.
for i in x:
    # 해당 부품이 존재하는지 확인한다.
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
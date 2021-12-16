n = int(input())
result = 0

# 한수를 판단하는 함수
def d(k):
    k_list = list(map(int, str(k)))
    if len(k_list) < 3:
        return True
    elif len(k_list) == 3:
        if k_list[1]-k_list[0] == k_list[2]-k_list[1]:
            return True
        else:
            return False
    else:
        return False


for i in range(1, n+1):
    # if 한수면 -> result + 1
    if d(i) == True:
        result = result + 1

print(result)
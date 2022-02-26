n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))

start = 0
end = n-1
isReturn = False
for target in m_list:
    while start <= end:
        mid = (start+end)//2
        if n_list[mid] == target:
            print("yes", end=' ')
            isReturn = True
            break
        elif n_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    start = 0
    end = n - 1

    if not isReturn:
        print("no", end=' ')
    isReturn = False
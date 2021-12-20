x = int(input())
group = 0
a = 0
b = 0
while x > group*(group+1)/2:
    group = group+1

# 해당 그룹 내에서 몇번째? -> K
k = x - (group-1) * (group) // 2

if x == 1:
    print("1/1")
    exit(0)

if group%2==0:
    # 순방향
    a = k
    b = group+1-a
else:
    b = k
    a = group+1-b

print("%d/%d"%(a,b))

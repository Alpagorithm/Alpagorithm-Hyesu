s = input()
row = int(s[1]) # 행
col = ord(s[0])-96 # 열
ans = 0

if col+2<=8:
    if row-1>=1:
        ans += 1
    if row+1<=8:
        ans += 1
if col-2>=1:
    if row-1>=1:
        ans += 1
    if row+1<=8:
        ans += 1
if col+1<=8:
    if row-2>=1:
        ans += 1
    if row+2<=8:
        ans += 1
if col-1>=1:
    if row-2>=1:
        ans += 1
    if row+2<=8:
        ans += 1
print(ans)
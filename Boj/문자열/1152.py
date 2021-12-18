str = input()
alphabet = []

for i in range(26):
    alphabet.append(0)

# 알파벳 개수 세기
for i in str:
    if ord(i) >= 97:
        alphabet[ord(i)-97] = alphabet[ord(i)-97] + 1
    else:
        alphabet[ord(i)-65] = alphabet[ord(i)-65] + 1

# 가장 많은 알파벳 대문자로 출력하기
max = 0
maxIdx = -1
for i in range(len(alphabet)):
    if max < alphabet[i]:
        max = alphabet[i]
        maxIdx = i

for i in range(len(alphabet)):
    if i != maxIdx and max == alphabet[i]:
        max = -1

if max == -1:
    print("?")
else:
    print(chr(maxIdx + 65))
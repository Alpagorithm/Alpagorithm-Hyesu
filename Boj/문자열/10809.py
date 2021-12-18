s = input()
alphabet = []

for i in range(0, 26):
    alphabet.append(-1)

for i in range(len(s)):
    if alphabet[ord(s[i])-97] == -1:
        alphabet[ord(s[i])-97] = i


for i in range(len(alphabet)):
    print(alphabet[i], end=" ")
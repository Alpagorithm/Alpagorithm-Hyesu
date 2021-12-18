n = int(input()) # 소문자 단어

# 단어 입력받기
wordList = []
for i in range(n):
    wordList.append(input())

# 그룹단어 체크하는 함수 True/False
def checkGroup(word):
    alphabet = []
    for i in range(26):
        alphabet.append(0)

    alphabet[ord(word[0])-97] = alphabet[ord(word[0])-97] + 1

    for i in range(1, len(word)):
        if word[i] != word[i-1] and alphabet[ord(word[i])-97] != 0:
            return False
        else:
            alphabet[ord(word[i]) - 97] = alphabet[ord(word[i])-97] + 1
    return True

result = 0

for i in range(len(wordList)):
    if checkGroup(wordList[i]) == True:
        result = result + 1

print(result)
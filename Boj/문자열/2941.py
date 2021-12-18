word = input() # 알파벳 소문자, - = 로만 이루어져 있는 최대 100글자 단어
list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in range(len(list)):
    word = word.replace(list[i], '1')

print(len(word))
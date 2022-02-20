# Swap in python
# 임시 저장공간 tmp를 만들 필요가 없다.

array = [3, 5]
array[0], array[1] = array[1], array[0]
print(array)
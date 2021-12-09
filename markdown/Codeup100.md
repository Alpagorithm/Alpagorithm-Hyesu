# 입출력 

```python
input()
```
한 줄 단위로 입력받는다.

<br>

## 한 번에 여러개 입력받기 - split()
```python
a, b = input().split()
```
split()을 이용하면 **split의 매개변수**를 기준으로 입력값을 잘라서 저장한다. split 의 기본 매개변수는 공백이다.

Ex) 공백을 기준으로 입력받기
```python
a, b = input().split()
```
입력: 1 2

a에 1, b에 2가 저장된다.

Ex) ,을 기준으로 입력받기
```Python
c, d = input().split(',')
```
입력: 1,2

c에 1, d에 2가 저장된다.

<br>

## 특정 포맷으로 출력하기 (16진수, 8진수, 유니코드값)

### 16진수
10진수를 입력받아 16진수로 출력하기
```python
# 16진수 대문자 - %X
a = int(input())
print("%X" %a)

# 16진수 소문자 - %x
b = int(input())
print("%x" %b)
```
ex) 대문자 16진수 출력 예시
![image](https://user-images.githubusercontent.com/68391767/145393235-74873bc7-4aac-4811-93ac-9c8e28713dcd.png)

### 8진수
```python
c = int(input())
print("%o" %c)
```

### 알파벳 -> 유니코드값
```python
n = ord(input())
print(n)
```

`ord()` 를 이용하면 문자를 10진수 유니코드값으로 변환할 수 있다.
- ord = ordinal position(어떤 문자의 순서 위치)
- A: 65, B: 66 ...
- 컴퓨터에 문자를 저장할 때 유니코드랑 아스키코드를 많이 사용한다.


### 유니코드값 -> 알파벳
```python
n = int(input())
print(chr(n))
```

`chr()` 를 이용하면 정수값을 문자로 바꿔준다.
- `ord()`와 반대다.

<br>
  
## 실수 출력하기
format을 사용하면 지정한 소수점 아래자리 까지의 정확도로 반올림한 값을 출력한다. (원하는 자리까지의 정확도로 반올림 된 실수값을 만들어준다.)

ex) 실수 1개를 입력받아 소숫점 이하 두 번재 자리까지 정확도로 반올림한 값
```python
a = float(input())
print(format(a, ".2f"))
```


<br>

# 문자열 다루기
## 문자열 더하기
- 문자열끼리 더하기(+)를 하면, 두 문자열을 합쳐서 연결한 결과를 만들어낸다.

- , 로 연결하면 띄어쓰기된 채로 연결된다.

``` python
print("김"+"혜수") #출력: 김혜수
print("김", "혜수") #출력: 김 혜수
```

<br>

## 문자열 여러번 출력하기 (문자열 곱하기)

`문자열 * 정수` 혹은 `정수 * 문자열`은 그 문자열을 여러번 반복한 문자열을 만들어준다.

```python
s = "알고리즘"
print(s * 3)

# 출력: 알고리즘알고리즘알고리즘
```
![image](https://user-images.githubusercontent.com/68391767/145395813-2a1c3006-f84d-4263-91b8-b68dd1be9b6a.png)
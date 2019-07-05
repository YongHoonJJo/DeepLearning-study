#### Hello Python



자료형

```
type() 함수로 특정 데이터의 자료형 확인 가능
```

<br>

변수

```
>>> x = 10
```

> 동적 언어로 런타임시 자료형이 결정된다.

<br>

주석

```python
# comment
```

<br>

리스트

```python
a = [1, 2, 3, 4, 5]
len(a)
a[0] = 99

# slicing 기능
a[0:2] # [99, 2], index 구간 [0, 2) 를 의미한다.
a[1:] # 인덱스 1부터 끝가지
a[:3] # 처음부터 인덱스 3전까지
a[:-1] # 처음부터 마지막 어ㅜㄴ소의 1개 앞가지
a[:-2] # 처음부터 마지막 원소 2개 앞까지
```

<br>

딕셔너리

```python
me = {'height': 180}
me['weight'] = 60
print(me) # {'weight': 60, 'height': 180}
```

> key 와 value 로 저장

<br>

bool

```python
hungry = True
sleepy = False
not hungry
hungry and sleepy
hungry or sleepy
```

> and, or, not 연산자 사용 가능

<br>

if 문

```python
if hungry:
  print("I'm hungry")
else:
  print("not yet")
```

<br>

for 문

```python
for i in [1, 2, 3]:
  print(i)
```

<br>

함수

```python
def hello():
  print('Hello')
  
hello()
```

<br>

클래스

```python
class Man:
  def __init__(self, name):
    self.name = name
    print('Initialized!')
    
  def hello(self):
    print('Hello ' + self.name + "!")
    
  def goodbye(self):
    print('bye-bye ' + self.name + '!')
    
m = Man('JJo')
m.hello()
m.goodbye()
```

> `__init__` 은 생성자이며, 첫 번째 매개변수로 self 를 명시적으로 쓰는 것이 특징.


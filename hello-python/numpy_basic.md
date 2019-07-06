#### Numpy_basic



```python
import numpy as np

# Numpy Array 생성
x = np.array([1.0, 2.0, 3.0])
print(x) # [1. 2. 3.]
print(type(x)) # <class 'numpy.ndarray'>

# Numpy 산술 연산
y = np.array([2.0, 4.0, 6.0])
print(x + y) # [3. 6. 9.]
print(x - y) # [-1. -2. -3.]
print(x * y) # [ 2.  8. 18.]
print(x / y) # [0.5 0.5 0.5]
print(x / 2.0) # [0.5 1.  1.5]

# Numpy - N차원 배열
A = np.array([[1, 2], [3, 4]])
print(A) # [[1 2]
         #  [3 4]]
print(A.shape) # (2, 2)
print(A.dtype) # int64

B = np.array([[3, 0], [0, 6]])
print(A + B) # [[ 4  2]
             #  [ 3 10]]
print(A * B) # [[ 3  0]
             #  [ 0 24]]
print(A * 10) # [[10 20]
              #  [30 40]]

# Broadcast
C = np.array([10, 20])
print(A * C) # [[10 40]
             #  [30 80]]

# 원소 접근
Z = np.array([[51, 55], [14, 19], [0, 4]])
print(Z) # [[51 55]
         #  [14 19]
         #  [ 0  4]]
print(Z[0]) # [51 55]
print(Z[0][1]) # 55

for row in Z:
    print(row)
# [51 55]
# [14 19]
# [0 4]
    
Z = Z.flatten()
print(Z) # [51 55 14 19  0  4] : 펼치기

print(Z[np.array([0, 2, 4])]) # [51 14  0] : 해당 인덱스의 요소를 가져옴

print(Z > 15) # [ True  True False  True False False]

print(Z[Z>15]) # [51 55 19]

```

<br>

넘파이의 산술 연산 : element-wise

배열의 형상은 shape 으로, 행렬에 담긴 원소의 자료형은 dtype 으로 확인

<br>

##### Broadcasting

![https://github.com/WegraLee/deep-learning-from-scratch/blob/master/ch01/images/fig%201-1.png?raw=true](https://github.com/WegraLee/deep-learning-from-scratch/blob/master/ch01/images/fig%201-1.png?raw=true)



![https://github.com/WegraLee/deep-learning-from-scratch/blob/master/ch01/images/fig%201-2.png?raw=true](https://github.com/WegraLee/deep-learning-from-scratch/blob/master/ch01/images/fig%201-2.png?raw=true)

<br>

1차원 배열 : vector

2차원 배열 : matrix

벡터와 행렬의 일반화 : tensor


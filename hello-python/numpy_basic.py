import numpy as np

# Numpy Array 생성
x = np.array([1.0, 2.0, 3.0])
print(x)
print(type(x))

# Numpy 산술 연산
y = np.array([2.0, 4.0, 6.0])
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x / 2.0)

# Numpy - N차원 배열
A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

B = np.array([[3, 0], [0, 6]])
print(A + B)
print(A * B)
print(A * 10)

# Broadcast
C = np.array([10, 20])
print(A * C)

# 원소 접근
Z = np.array([[51, 55], [14, 19], [0, 4]])
print(Z)
print(Z[0])
print(Z[0][1])

for row in Z:
    print(row)

Z = Z.flatten()
print(Z)

print(Z[np.array([0, 2, 4])])

print(Z > 15)

print(Z[Z>15])

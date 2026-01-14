#### Define a new zero-value matrix（零行列）, for example, a 3x3 matrix A:
```python
A = np.zeros((3, 3))
```

#### Define a new known-value matrix, for example, a [0, 0, 1] matrix A:
```python
A = np.array([0, 0, 1])
```

#### Dot Product（内積）of matrices A & B
```python
C = A @ B
```

#### Cross Product（外積）of matrices A & B
```python
C = np.cross(A, B)
```
#### Transpose of a matrix A（転置行列）
```python
A -> A.T
```

#### Inverse of a matrix A（逆行列）
```python
A -> np.linalg.inv(A)
```

#### Length of a vector A（ベクトルの大きさ）
```python
length = np.linalg.norm(A)
```

#### Flatten a vector A（平坦化）
```python
flatten_A = A.ravel()
```

#### 配列の形状を変換するreshapeの使い方、例：A（height, width, 1) -> A（height*width, 1)
```python
A -> A.reshape(-1, 1)
```


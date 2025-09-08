# 📊 NumPy (Numeric Python)

NumPy is a Python library used for numerical computations.
It provides support for arrays, mathematical functions, and is widely used in Data Science, Machine Learning, and Scientific Computing.

## 🔹 Why NumPy?

- Works faster than Python lists.

- Provides multidimensional arrays.

- Supports vectorized operations (no need for loops).

- Has many mathematical and statistical functions.

## 🔹 Installation

```bash
pip install numpy
```

🔹 Importing NumPy
```python
import numpy as np # here np is aleas which is a conviction from python community. you can write your own as well.
```

## 🔹 Creating Arrays

```python
import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4])
print("1D Array:", arr1)

# 2D array (Matrix)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Array of zeros
zeros = np.zeros((3, 3))
print("Zeros Array:\n", zeros)

# Array of ones
ones = np.ones((2, 4))
print("Ones Array:\n", ones)

# Range of numbers
rng = np.arange(1, 10, 2)   # start=1, stop=10, step=2
print("Range Array:", rng)

# Evenly spaced numbers
lin = np.linspace(0, 1, 5)   # 5 values between 0 and 1
print("Linspace Array:", lin)
```

## 🔹 Array Properties
```python

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr.shape)   # (rows, columns)
print("Size:", arr.size)     # total elements
print("Dimension:", arr.ndim) # 2D
print("Datatype:", arr.dtype)

```

## 🔹 Basic Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Dot Product:", np.dot(a, b))
```

## 🔹 Indexing & Slicing


```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])     # first element
print(arr[-1])    # last element
print(arr[1:4])   # slice [20, 30, 40]

# 2D Slicing
mat = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print(mat[0, 1])     # first row, second column (2)
print(mat[:, 1])     # all rows, second column
print(mat[1:, :2])   # sub-matrix [[4,5],[7,8]]
```

## 🔹 Useful Functions

```python
arr = np.array([1, 2, 3, 4, 5])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Square Root:", np.sqrt(arr))
```

### Sources
[numpy](https://numpy.org/)
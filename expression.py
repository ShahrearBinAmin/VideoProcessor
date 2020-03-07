import numpy as np

nums = [1, 2, 3, 4, 5, 6]

squares = [x ** 2 for x in nums if x % 2 == 0]
print(squares)

b = np.array([[1, 2, 3],
              [4, 5, 6]])


print(b)
print(b.shape)
print(b[0,1])


# Tutorial on Numpy python library.
import numpy as np

arr = [[6,7,8,9],[1,2,3,4]]
a = np.array(arr)

print(a.shape)
print(a.ndim)
print(a[0][-1])

b = np.array([1,2,3,4], ndmin = 5)
print(b)
print(b.shape)
print("The dimension is {}" .format(b.ndim))
print(2/a)


c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c)
print(c.shape)
print(c.ndim)

d = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(d.shape)
print(d.ndim)

e = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(e[:2, 1:4])
import numpy as np 
import matplotlib as plt
import urllib.request 

array_1 = np.random.randint(256, size=(200,200))
array_2 = np.random.randint(256, size=(200,200))
array_3 = np.random.randint(256, size=(200,200))

matrix = np.array([[array_1], [array_2], [array_3]])

print(matrix)


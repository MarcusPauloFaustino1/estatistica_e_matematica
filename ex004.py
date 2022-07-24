import numpy as np 

numbers = np.arange(10)

for i in numbers:
    if i % 2 != 0:
        numbers[i] = -1

print(numbers)
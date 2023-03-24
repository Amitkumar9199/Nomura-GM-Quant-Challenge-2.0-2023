import numpy as np
import math

p = math.pi / 4
n = 100

result = np.sum(np.array([np.math.comb(n, k) * (p**k) * ((1-p)**(n-k)) for k in range(79, 101)]))

print("The probability that more than 78 points lie inside the inscribed circle is:")
print(result)

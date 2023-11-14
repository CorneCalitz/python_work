"""
How does total inventory change as the number of stocking points changes?

n[1] = number of existing facilities
n[2] = number of future facilities
x[1] = total inventory in present facilities
x[2] = total inventory in future facilities

x[2] = x[1] * sqrt(n[2]/n[1])
"""

import math

n1 = 3
n2 = 12
x1 = 3000
x2 =x1 * math.sqrt(n2/n1)
print(x2)
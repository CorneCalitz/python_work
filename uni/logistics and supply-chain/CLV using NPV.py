"""
NPVa = P * [(1-(1+i)^-n)/i]

A = customer a
P = average annual profit, or (annual sales * profit margin)
i = annual discount rate, and
n = expected lifetime in years
"""

def calc_clv(P, i, n):
    return P * ((1-(1+i)**-n)/i)

print("A:",calc_clv(4500*0.15, 0.08, 10))
print("B:",calc_clv(4000*0.14, 0.08, 8))





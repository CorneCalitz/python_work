import math


def eoq(R, S, C, k):
    # Holding cost($)
    H = k * C

    # Returns number of units
    return math.sqrt((2 * R * S) / H)


R = 50_000  # Annual demand (units)
S = 150  # Cost per order ($)
C = 100  # Cost per unit ($)
k = 0.15  # Holding cost (%)


if __name__ == "__main__":
    print(eoq(R, S, C, k))

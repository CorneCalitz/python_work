"""
TAIC = Annual purchase cost + Annual holding cost + Annual order cost
TAIC = APC + AHC + AOC = (R*C) + (Q/2 * k * C) + (R/Q * S)

"""

from EOQ import eoq


def TAIC(R,S,k,C,Q):
    APC = R * C
    AHC = (Q/2 * k * C)
    AOC = R / Q * S
    TAIC = APC + AHC + AOC
    print("Economic order quantity", Q)
    print("Purchase cost", APC)
    print("Holding cost", AHC)
    print("Order cost", AOC)
    print("Total annual inventory cost", TAIC)

if __name__ == "__main__":
    R = 100
    S = 150
    k = 0.15
    C = 100
    Q = eoq(R, S, C, k)

    TAIC(R,S,k,C,Q)



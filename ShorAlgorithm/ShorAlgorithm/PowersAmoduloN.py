import matplotlib.pyplot as plt
import numpy as np

def powersAModuloN(a,N):
    powers = []
    for i in range(N):
        powers.append(a**i % N)
    return powers

def powersAModuloNRecursive(a,N):
    powers = []
    powers.append(1)

    for i in range(1, N):
        powers.append((powers[i-1] * a) % N)
    return powers

def findPeriod(a, N):
    powers = powersAModuloNRecursive(a, N)
    return powers.index(1,1)

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

if __name__ == '__main__':
    N = 23
    a = 2
    powers_a_N = powersAModuloNRecursive(a,N)
    xpoints = np.array(range(N))
    ypoints = np.array(powers_a_N)

    print("f_a_N=", powers_a_N)
    period = findPeriod(a, N)
    print("period of f_a_N", period)

    print("a^(period/2) Mod N = ", (a**(period/2)) % N)
    print("(-1) Mod N= ",  (-1) % N)
    print("factor1= ", gcd((a**(period/2)) + 1, N))
    print("factor2= ", gcd((a**(period/2)) - 1, N))

    print((a**(period/2)) +1)
    print(gcd(161,371))

    plt.bar(xpoints, ypoints)
    plt.show()

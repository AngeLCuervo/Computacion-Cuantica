import matplotlib.pyplot as plt
import numpy as np

def powersAModuloN(a,N):
    powers = []
    for i in range(N):
        powers.append(a**i % N)
    return powers

def periodoDeF(a,N):
    powers =powersAModuloN(a,N)
    return powers.index(1,1)

if __name__ == '__main__':
    N = 15
    a = 2
    powers_a_N = powersAModuloN(a,N)
    print("Periodo: ", periodoDeF(a, N))
    xpoints = np.array(range(N))
    ypoints = np.array(powers_a_N)

    print("f_a_N=", powers_a_N)
    plt.bar(xpoints, ypoints)
    plt.show()
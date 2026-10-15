import math as m


def factors(n):
    factors = []

    factors.append(1)
    if n % 2 ==0:
        factors.append(2)

    factor = 3
    for i in range(n):
        if n % factor == 0:
            factors.append(factor)
        factor = factor + 1

    return factors

def primes():
    primes = []
    for i in range(1, 1000):

        fact = factors(i)
        if len(fact) == 2:
            print(i, " is prime")
            primes.append(i)
        if len(fact) > 2:
            print(i, " is composite with factors ", fact)
    print(primes)
    print(len(primes))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(primes())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

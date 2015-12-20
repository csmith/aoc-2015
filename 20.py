from itertools import chain

target = 34000000

flatten = chain.from_iterable
factors = lambda n: set(flatten((i, n//i) for i in range(1, int(n**0.5)+1) if n % i == 0))
presents1 = lambda n: 10 * sum(x for x in factors(n))
presents2 = lambda n: sum(11 * x for x in factors(n) if n // x <= 50)

print(next(i for i in range(target) if presents1(i) > target))
print(next(i for i in range(target) if presents2(i) > target))

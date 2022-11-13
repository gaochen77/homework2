def fib_relapse(n):
    assert n >= 1, "n > 1"
    if n <= 2:
        return n
    if n == 3:
        return fib_relapse(n - 2)
    else:
        return fib_relapse(n - 2) + fib_relapse(n - 3)


for i in range(2, 33):
    print(fib_relapse(i), end='@')

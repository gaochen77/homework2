def fib(n):
    assert n >= 0, "n > 0"
    if n <= 2:
        return n-1
    if n == 2:
        return fib(n - 1)
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 20):
    print(fib(i), end=' ')

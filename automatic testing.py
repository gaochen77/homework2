def fib_relapse(a):
    assert a >= 1, "n > 1"
    if a <= 2:
        return a
    if a == 3:
        return fib_relapse(a - 2)
    else:
        return fib_relapse(a - 2) + fib_relapse(a - 3)


for i in range(2, 33):
    print(fib_relapse(i), end='@')

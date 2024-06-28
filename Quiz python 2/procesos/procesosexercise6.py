def fibonacci(n):
    fib_seq = [0, 1]

    while len(fib_seq) < n:
        next_term = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_term)

    return fib_seq
# Display the first n numbers in the fibonacci sequence

from typing import Iterator


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b


print("Hello", fib(10))

"""An example of recursive functions."""


def factorial(n: int) -> int:
    """Compute the factorial of n."""

    # Base Case: n is 0 or 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: n * recursive call with n-1 as argument
    else:
        return n * factorial(n - 1)


# Example usage
print(factorial(3))

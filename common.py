def get_factors(num):
    """Return a list of factors for num.

    >>> get_factors(6)
    [1, 2, 3, 6]

    >>> get_factors(12)
    """
    factors = []

    # Extend range by 1 to include num
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    return factors


def is_prime(num):
    """Return whether a number is prime.

    >>> is_prime(2)
    True

    >>> is_prime(14)
    False

    >>> is_prime(23)
    True
    """
    # 2 is prime; exclude
    if num == 2: 
        return True
    
    # exclude all other even numbers and numbers less than 2
    if num % 2 == 0 or num < 2:
        return False
    
    # Only need to count up to the the square root of num
    sqrt = int(num ** 0.5 +1)  # int rounds down; correct by +1
    
    # Loop through all odd numbers
    for i in range(3, sqrt, 2):
        if num % i == 0:
            return False
    return True



def factorial(num):
    """Return the factorial for num.

    >>> factorial(6)
    720

    >>> factorial(9)
    362880

    >>> factorial(0)
    1

    """
    result = 1

    if num == 0:
        return 1

    for i in range(num, 1, -1):
        result *= i
    return result


def fibonacci(num):
    """Return a list of the first n fibonacci numbers.

    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    
    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    """
    counter = 0

    # Start fibonacci
    sequence = [0, 1]
    while len(sequence) < num:
        n1 = sequence[counter]
        n2 = sequence[counter + 1]
        sequence.append(n1+n2)

        counter += 1

    return sequence


def to_roman(numeral):
    """
    The key is to divide numeral by each roman and multiply the symbol by the
    quotient. Use the remainder to complete the rest of the numbers.
    """
    mapping = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    romans = {v:k for k,v in mapping.items()}
    result = ''

    for divisor, symbol in romans.items():
        count = numeral // divisor
        remainder = numeral % divisor
        numeral = remainder
        result += symbol * count

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

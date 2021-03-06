'''Playing around with implementing the p-adic norm in Python.'''
from fractions import Fraction
import primes


def validate_prime(p):
    if not primes.prime_check(p):
        raise ValueError


def find_p_ord_int(a, p):
    '''Calculate the ordinal of a, an int, with respect to p a prime.'''
    if a == 0:
        validate_prime(p)
        return float("inf")
    elif isinstance(a, Fraction):
        raise 'Error a is a fraction must be an int.'
    try:
        a = int(a)
    except ValueError:
        raise ValueError
    validate_prime(p)
    c = 0
    while a % (p**c) == 0:
        c += 1
    return c - 1


def find_p_ord(a, p):
    '''Calculate the ordinal of a rational number a
        with respect to a prime p.'''
    if a == 0:
        validate_prime(p)
        return float("inf")
    elif isinstance(a, int):
        return find_p_ord_int(a, p)
    else:
        try:
            frac = Fraction(a).limit_denominator()
        except ValueError:
            raise ValueError
        numerator = find_p_ord_int(frac.numerator, p)
        denominator = find_p_ord_int(frac.denominator, p)
        return numerator - denominator


def p_norm(a, p):
    '''Calculate the p-adic norm of a, a rational number,
    with repect to p a prime.'''
    return 1/(p**find_p_ord(a, p))


def p_metric(a, b, p):
    '''Calculate the distance between a and b, both rational numbers,
        in the p-adic space of a prime p.'''
    return p_norm(a-b, p)

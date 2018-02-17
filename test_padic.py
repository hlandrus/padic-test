import padic
import random
import primes
from fractions import Fraction

max_prime = 1000
list_primes = primes.create_prime_list()


def test_ordab_eq_orda_plus_ordb():
    '''Test property that ord_p(ab) == ord_p(a) + ord_p(b)
        over 10000 random integers for first five primes'''
    for i in range(10000):
        p = get_random_prime(5)
        a = random.randint(-10000, 10000)
        b = random.randint(-10000, 10000)
        error_message = \
            f'ord {p} of {a} + ord {p} of {b} != to ord {p} of {a} times {b}'
        a_ord = padic.find_p_ord(a, p)
        b_ord = padic.find_p_ord(b, p)
        ab_ord = padic.find_p_ord(a*b, p)
        assert a_ord + b_ord == ab_ord, error_message


def test_positive_unless_zero():
    '''Test property that |a|_p = 0 iff a=0 and |a|_p > 0
        over 10000 random integers for first five primes'''
    for i in range(10000):
        p = get_random_prime(5)
        a = random.randint(-10000, 10000)
        a_norm_p = padic.p_norm(a, p)
        error_message_zero = f'The {p}-Adic norm of {a} is not zero.'
        error_message_non_zero = f'The {p}-Adic norm of {a} is zero.'
        error_message_non_positive = f'The {p}-Adic norm of {a} is negative.'
        if a == 0:
            assert a_norm_p == 0, error_message_zero
        else:
            assert a_norm_p != 0, error_message_non_zero
            assert a_norm_p > 0, error_message_non_positive


def test_multiplicative():
    '''Test property that |ab|_p == |a|_p |b|_p
        over 10000 random integers for first five primes'''
    for i in range(10000):
        p = get_random_prime(5)
        a = random.randint(-10000, 10000)
        b = random.randint(-10000, 10000)
        error_message = f'|{a} * {b}|_{p} not equal to |{a}|_{p} * |{b}|_{p}'
        a_norm_p = padic.p_norm(a, p)
        b_norm_p = padic.p_norm(b, p)
        ab_norm_p = padic.p_norm(a*b, p)
        frac_a_b_norm_p = Fraction(a_norm_p * b_norm_p).limit_denominator()
        frac_ab_norm_p = Fraction(ab_norm_p).limit_denominator()
        assert frac_a_b_norm_p == frac_ab_norm_p, error_message


def test_triangle_inequality():
    '''Test property that |a+b|_p <= |a|_p + |b|_p
        over 10000 random integers for first five primes'''
    for i in range(10000):
        p = get_random_prime(5)
        a = random.randint(-10000, 10000)
        b = random.randint(-10000, 10000)
        a_norm_p = padic.p_norm(a, p)
        b_norm_p = padic.p_norm(b, p)
        ab_norm_p = padic.p_norm(a*b, p)
        error_message = f'|{a} + {b}|_{p} is > than |{a}|_{p} + |{b}|_{p}'
        assert ab_norm_p <= a_norm_p + b_norm_p, error_message


def get_random_prime(n):
    return list_primes[random.randint(0, n)]


if __name__ == '__main__':
    test_ordab_eq_orda_plus_ordb()
    test_positive_unless_zero()
    test_multiplicative()
    test_triangle_inequality
    print('All passed')

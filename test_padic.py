import pAdic
import random
import primes
from fractions import Fraction

max_prime = 1000
list_primes = primes.create_prime_list()

def test_if_divisible_not_prime():
    for i in range(10000):
        a = random.randint(2,10)
        b = random.randint(1,max_prime)
        if b%a == 0 and a != b :
            error_message = f'{b} is divisible by {a} so not prime.'
            assert primes.prime_check(b) == False, error_message

def test_if_prime_then_no_divisors():
    for i in range(10000):
        a = random.randint(1,max_prime)
        if primes.prime_check(a):
            for j in range(2, int(a/2)):
                error_message = f'{a} is divisible by {j} so not prime.'
                assert a%j, error_message

def test_ordab_eq_orda_plus_ordb():
    for i in range(10000):
        p = get_random_prime(5)
        a = random.randint(-10000,10000)
        b = random.randint(-10000,10000)
        error_message = f'ord {p} of {a} + ord {p} of {b} not equal to ord {p} of {a} times {b} '
        assert pAdic.find_p_ord(a,p) + pAdic.find_p_ord(b,p) == pAdic.find_p_ord(a*b,p), error_message 

def test_positive_unless_zero():
    for i in range(10):
        p = get_random_prime(5)
        a = random.randint(-10000,10000)
        norm_p_of_a = pAdic.p_norm(a,p)
        error_message_zero = f'The {p}-Adic norm of {a} is not zero.'
        error_message_non_zero = f'The {p}-Adic norm of {a} is zero.'
        error_message_non_positive = f'The {p}-Adic norm of {a} is negative.'
        if a == 0:
            assert norm_p_of_a == 0, error_message_zero
        else:
            assert norm_p_of_a != 0, error_message_non_zero
            assert norm_p_of_a > 0, error_message_non_positive

def test_multiplicative():
    for i in range(10000):
        p = get_random_prime(5)
        a = random.randint(-10000,10000)
        b = random.randint(-10000,10000)
        error_message = f'|{a} * {b}|_{p} not equal to |{a}|_{p} * |{b}|_{p}'
        norm_p_of_a = pAdic.p_norm(a,p)
        norm_p_of_b = pAdic.p_norm(b,p)
        norm_p_of_ab = pAdic.p_norm(a*b,p)
        frac_norm_p_of_a_b = Fraction(norm_p_of_a * norm_p_of_b).limit_denominator() 
        frac_norm_p_of_ab = Fraction(norm_p_of_ab).limit_denominator() 
        assert frac_norm_p_of_a_b == frac_norm_p_of_ab, error_message 

def test_triangle_inequality():
    for i in range(10000):
        p = get_random_prime(5)
        a = random.randint(-10000,10000)
        b = random.randint(-10000,10000)
        norm_p_of_a = pAdic.p_norm(a,p)
        norm_p_of_b = pAdic.p_norm(b,p)
        norm_p_of_ab = pAdic.p_norm(a*b,p)
        error_message = f'|{a} + {b}|_{p} is greater than |{a}|_{p} + |{b}|_{p}'
        assert norm_p_of_ab  <= norm_p_of_a + norm_p_of_b, error_message
    
            
def get_random_prime(n):
    return list_primes[random.randint(0,n)]
    
    
        
if __name__ == '__main__':
    test_if_divisible_not_prime()
    test_if_prime_then_no_divisors()
    test_ordab_eq_orda_plus_ordb()
    test_positive_unless_zero()
    test_multiplicative()
    test_triangle_inequality
    print('All passed')
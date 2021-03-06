import primes
import random

max_prime = 1000
list_primes = primes.create_prime_list()


def test_if_divisible_not_prime():
    '''Test property that if a|b then b cannot be prime.'''
    for i in range(10000):
        a = random.randint(2, 10)
        b = random.randint(1, max_prime)
        if b % a == 0 and a != b:
            error_message = f'{b} is divisible by {a} so not prime.'
            assert not primes.prime_check(b), error_message


def test_if_prime_then_no_divisors():
    '''Test that if a is prime then no int will divide a. Can stop at a/2.'''
    for i in range(10000):
        a = random.randint(1, max_prime)
        if primes.prime_check(a):
            for j in range(2, int(a/2)):
                error_message = f'{a} is divisible by {j} so not prime.'
                assert a % j, error_message


if __name__ == '__main__':
    test_if_divisible_not_prime()
    test_if_prime_then_no_divisors()
    print('All Passed')

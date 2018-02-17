'''A collection of functions relating to the testing of primes'''


def create_seive(n):
    '''Creates a list of primality of integers up to n.
    n Should be an positive, if not integer will round down to closest int '''
    try:
        n = int(n)
    except ValueError:
        raise ValueError

    assert n > 0

    my_list = [True] * (n+1)
    my_list[0] = False
    my_list[1] = False

    for j in range(2, n//2 + 1):
        for i in range(j, n+1, j):
            if i != j:
                my_list[i] = False

    return my_list


max_prime = 1000
is_prime_list = create_seive(max_prime)


def create_prime_list():
    '''Creates a list of primes up to n.
    n Should be an positive, if not integer will round down to closest int '''
    prime_list = []
    for i, j in zip(is_prime_list, range(0, max_prime)):
        if i:
            prime_list.append(j)
    return prime_list


def prime_check(p):
    '''Given a p check that it is a prime number between 0 and 1000'''
    try:
        p = int(p)
        is_prime = is_prime_list[p]
    except ValueError:
        return False
    return is_prime

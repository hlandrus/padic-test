# The p-Adic Norm and Property Based Testing
This repo originated from two motivations. Implementing the p-Adic norm which has some unusual properties and playing with property based testing. These things fit well together since the p-Adic norm has some proven mathematical properties that can be used to help test an implementation of it.

# Files
Using_pAdic_Norm.ipynb is a notebook that explains the p-Adic norm and uses the functions in the remaining files. 

primes.py has functions to help test primes up to 1000, used to validate the prime being considered is valid.

pAdic.py has functions related to calculating the ordinal, norm and metric with respect to a prime p.

test_padic.py tests the functions in pAdic.py using the mathematical properties of the functions.

test_primes.py test the functions in primes.py using properties of primes and composite numbers.
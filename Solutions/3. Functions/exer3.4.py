"""
    Primes
    Author: Stefanos Kalogerakis
    Last Modified: 22/10/2021
"""


# (a) Write a function is_prime(n) that returns True only if n is prime.
# (b) Note that apart from 2 and 3, all primes are of the form 6k ± 1 (though not all numbers of the
# form 6k ± 1 are prime of course). Using this, we can improve the computation time by a factor 3. Update your function to use this.
# (c) Write a function that returns all primes up to n.
# (d) Write a function that returns the first n primes.

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True


val = 53
print('Question a, val ',val,' is ', is_prime(val))


# Modify the logic of the code given the equation from the assignment. 
def is_prime_b(x):
	if x < 2:
		return False
	elif x == 2 or x == 3:
		return True
	else:
		counter = 1
		prime_val1 = 0
		prime_val2 = 0
		while(x>=prime_val1 and x>= prime_val2):
			prime_val1 = 6 * counter + 1
			prime_val2 = 6 * counter - 1
			if(x == prime_val1 or x == prime_val2):
				return True
			counter+=1
		return False


print('Question b, val ',val,' is ', is_prime_b(val))

# Since the whole logic is implemented simply print the prime numbers. I just print them, could use a list to store them
def primes_ret(x):
	
	for i in range(1,x):
		if is_prime_b(i) == True:
			print(i)

primes_ret(100)
'''
Question 1:

Assymetric scheme(RSA) is slower than symetric alternative (AES) because RSA algorithm is base on 
the matematical problem  of factoring large  prime numbers.  It uses complex mathematical calculation 
to generate  large keys (often 2048 bits or 4096 bits) . These computation make it slower but very secure.

AES in the other hand oparate a much smuller key size works with fixed block sizes (often 128, 192, or 256 bits).
It required less computing power this make it slower 

An attacker can access information such ass
public key, the incripted message and the encryption algorithm
but however without the private key this information are useless
it is nearly impossible to generate the private key base on the publik key 

'''
# Task 1

def prime(n):
    is_prime = True
    for i in range (2, n):
        if n % i == 0:
            is_prime = False
            break

    if  is_prime:
        print(f'{n} is prime')
        return n
    else:
        print(f'{n} is not prime')
        return None

        
'''
    Answer to Question 2:
    I will depend on the number it self . 
    In our case all posif numbers starting form 2 will be tested until the function finds first  divisor.
    If the  function at least or the loop will break and the decision will be made. 
    Other wise all numbers less than n will be tested.
    
    '''

def find_gcd(c, d):
    if c < d:
        c , d = d , c
    while d != 0 :
        c, d = d, c % d 
    return c
    
def is_relatively_prime(n1, n2):
    gcd = find_gcd(n1, n2)
    if gcd == 1:
        return gcd
    else:
        return False
    

# Task 2
def EEA(a, b):
    relatvly_prime_state = is_relatively_prime(a, b)
    if relatvly_prime_state:
        x0 = b
        x1, x2 = 1, 0
        y1, y2 = 0, 1

        while b!= 0:
            r, a, b = a//b, b, a % b
            x1, x2 = x2, x1 - r * x2
            y1, y2 = y2, y1 - r * y2
        return x1 % x0
    else:
        return None 
        
def invers_of_a_mod_b(e, f):
    inverse= EEA(e,f)

    if inverse is not None:
        print(f'The inverse of {e}(mod {f}) is {inverse}')
    else:
        print(f'There is no inverse for {e}(mod {f})')


# Task 3:
def Eulerphi(N):
    result = 0
    for i in range(1, N):
        if find_gcd(1, N)==1:
            result += 1
    return result

# task 4:
def invers_of_a_mod_b(e, modulus):
    inverse= EEA(e,modulus)
    if inverse is not None:
        return inverse


'''
Answer to Question 3:
pk = (e, N) = (19,77)
m = 15
e = 19
N = 77
c = (m^e) mod N
c = (15^19) mod 77

15^19 mod 77 = (15^1 * 15^2 * 15^16) mod 77

15^1 mod 77 = 15
15^2 mod 77 = (15 * 15) mod 77 = 225 mod 77 = 71
15^4 mod 77 = (71 * 71) mod 77 = 5041 mod 77 = 36
15^8 mod 77 = (36 * 36) mod 77 = 1296 mod 77 = 64
15^16 mod 77 = 64 * 64 mod 77 = 4096 mod 77 = 15

c = (15^1 * 15^2 * 15^16) mod 77 
    =((15^1 mod 77) * (15^2 mod 77) * (15^1 mod 77)) mod77
    =(15 * 71 * 15) mod 77 = 15975 mod 77 
    = 36

c = 36

'''

if __name__ == "__main__":
    print('prime numbers')
    prime_test= [2, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for p in prime_test:
        print(f"{p} is prime: {prime(p)}")
    print('icke prime')
    
    test_icke_prime= [4, 6, 8, 10, 12, 14, 20,30,40,50,60,70,80]
    for p in test_icke_prime:
        print(f"{p} is not prime: {prime(p)}")
   

print()
print(30%12)
print(is_relatively_prime(20, 3))
print(is_relatively_prime(20, 3))  # True (since GCD is 1)
print(is_relatively_prime(20, 5))  # False (since GCD is 5)
print(is_relatively_prime(35, 64)) # True (since GCD is 1)
print( " EEA")
invers_of_a_mod_b(2, 11 )
print(prime(2))
print(invers_of_a_mod_b(3, 11))


 
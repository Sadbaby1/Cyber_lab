'''
Question 1:




'''
# Task 1

def prime(n):
    is_prime = True
    for i in range (2, n):
        #print(f' i är {i}')
        if n % i == 0:
            is_prime = False
            #print(f' är {i}')
            break

    if  is_prime:
        print(f'{n} is prime')
        #return n 
    else:
        print(f'{n} is not prime')
              
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
    
def is_relatvly_prime(n1, n2):
    gcd = find_gcd(n1, n2)
    if gcd == 1:
        return gcd
    else:
        return False
    

# Task 2
def EEA(a, b):
    relatvly_prime_state = is_relatvly_prime(a, b)
    print("a")
    if relatvly_prime_state:
        print("b")
        invers_of_a_mod_b = 1/(a % b)
        print(f'The inverse of a(mod b) is {invers_of_a_mod_b}')



if __name__ == "__main__":
    print('prime numbers')
    prime(2)
    prime(3)
    prime(5)
    prime(11)
    prime(13)
    prime(17)
    prime(19)
    prime(23)
    prime(29)
    prime(31)
    prime(37)
    prime(41)
    prime(47)
    prime(53)
    prime(59)
    prime(61)
    prime(67)
    prime(71)
    prime(73)
    prime(79)
    prime(83)
    prime(89)
    prime(97)
    print('icke prime')
    prime(4)
    prime(6)
    prime(8)
    prime(10)
    prime(12)
    prime(14)
    prime(100)
    prime(300)
    for k in range(1,10):
        print(k)
        

    print("Extra")
    for k in range(1,10):
        if 10 % k == 0:
            print(k)

    print()      
    print("Extra med beak statment")
    for k in range(1,10):
        if 10 % k == 0:
            print(k)
            break

    
    print()
    print("int !=0 ")
    for k in range(1,10):
        
        if 10 % k != 0:
            print(k)

print()
print(30%12)
print(is_relatvly_prime(20, 3))
print(is_relatvly_prime(20, 3))  # True (since GCD is 1)
print(is_relatvly_prime(20, 5))  # False (since GCD is 5)
print(is_relatvly_prime(35, 64)) # True (since GCD is 1)
print( " EEA")
EEA(20, 30 )
 
import sympy


def generate_numbers_in_corners_of_n_th_wrap( last_number, n ):
    if n==0: 
        return (1,[])
    else:
        next_last_number =  last_number + 4+4+2*4*(n-1)
        length_of_side = 2 + 1 + (n-1)*2
        print( "debug: length of side:", length_of_side ) 
        k = last_number + length_of_side - 1
        k1 = k + length_of_side - 1
        k2 = k1 + length_of_side - 1 
        k3 = k2 + length_of_side - 1
        
        return (next_last_number, [k,k1,k2,k3])
    


number_of_primes = 0 
total_numbers = 1 
n = 1
last_number = 1
perc = 1
while perc > 0.1:
    (last_number, numbers) = generate_numbers_in_corners_of_n_th_wrap( last_number, n )
    print( n, last_number, numbers )
    for k in numbers: 
        if sympy.isprime(k): 
            number_of_primes += 1

    if n>0: 
        total_numbers+=4
    perc = number_of_primes/ total_numbers
    print(f"{number_of_primes} / {total_numbers} = {perc}")
    n+=1

     

      

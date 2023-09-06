


def generate_numbers_in_corners_of_n_th_wrap( last_number, n ):
    if n==0: 
        return (1,[])
    else:
        next_last_number =  last_number + 4+4+2*n
        length_of_side = 1 + (n)*2 
        k = last_number + length_of_side - 2
        k1 = k + length_of_side - 1 
        k2 = k1 + length_of_side - 1 
        k3 = k2 + length_of_side - 1
        
        return (next_last_number, [k,k1,k2,k3])
    

last_number = 0
for n in range( 0, 4 ):
    (last_number, numbers) = generate_numbers_in_corners_of_n_th_wrap( last_number, n )
    print( last_number, numbers )
     

      

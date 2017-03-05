def find_in_tree(ln, ld, un, ud, converge_to_dec, error):
    '''
    Using the Stern_Brocot Tree,
    we have lower and upper bounds for both the numerator and the denominator
        find_in_tree(lower_numerator, lower_denominator, 
            upper_numerator, upper_denominator, converge_to)
    converge_to_dec < 1
    '''

    # The mediant is (ln+un)/(ld+ud)
    middle_n = ln + un
    middle_d = ld + ud
    
    # Binary search 
    if converge_to_dec + error < middle_n / middle_d:
        return find_in_tree(ln, ld, middle_n, middle_d, converge_to_dec, error)
    elif converge_to_dec - error > middle_n / middle_d:
        return find_in_tree(middle_n, middle_d, un, ud, converge_to_dec, error)
    else:
        return (middle_n, middle_d)

def dec_to_frac (x, error = 0.00000000001):
    integer = int(math.floor(x))
    decimal = x - integer

    if decimal < error:
        # Close enough to an integer defined by error
        return [integer, 1]
    elif decimal > (1-error):
        # Close enough to the next whole integer
        return [integer+1, 1]

    # The Stern-Brocot Tree may help us here!
    final_n, final_d = find_in_tree(0,1,1,1,decimal,error)
    return [integer * final_d + final_n, final_d]

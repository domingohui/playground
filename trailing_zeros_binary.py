def count_trailing_zeros_in_binary(n):
    # http://graphics.stanford.edu/~seander/bithacks.html#ZerosOnRightLinear
    # Exclusive OR on n and (n-1)
    # To turn trailing 0's into 1's
    # Then shift right by 1 bit
    binary = (n ^ (n-1)) >> 1

    # Now all trailing 0's are 1's
    # Digits before the trailing 0's are canceled to 0's after the XOR operation
    # Keep shifting right until number becomes 0
    counter = 0
    while binary:
        binary >>= 1
        counter += 1

    return counter

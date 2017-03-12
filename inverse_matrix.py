def inverse (m):
    '''
    m = [ [...], [...] ... ]
    m must be square matrix. len(m) == len(m[0])
    '''

    dim = len(m)

    augmented = []
    
    # 1) Augment the matrix
    for row_index in range(dim):
        augmented.append(m[row_index] + 
                [Fraction(0)] * row_index + 
                [Fraction(1)] + 
                [Fraction(0)] * (dim - row_index - 1))

    print(augmented)

    # 2) Elimination - Clear a column 
    # to turn rows into reduced row-echelon form.
    # https://people.richland.edu/james/lecture/m116/matrices/pivot.html
    for r in range(dim):
        for c in range(dim):
            # Clear each column
            if r != c:
                # Pivot element
                ratio = augmented[c][r]/augmented[r][r]
                for k in range(dim*2):
                    augmented[c][k] = augmented[c][k] - ratio * augmented[r][k]

    # 3) Apply ratios(multiples) in diagonal entries
    # to reduce entries in rhs of the augmented matrix to simplest form
    for r in range(dim):
        multiple = augmented[r][r]
        for c in range(dim*2):
            augmented[r][c] /= multiple
    
    to_return = [ [element for element in row[dim:]] for row in augmented]

    return to_return

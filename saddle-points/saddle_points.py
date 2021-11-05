def saddle_points(matrix):

    # Check matrix has regular shape
    if matrix:
        for i in range(len(matrix)-1):
            if (len(matrix[i-1])!=len(matrix[i])):
                raise ValueError("ValueError")
    else:
        return []

    # Get transpose of matrix
    matrixT = [[j[i] for j in matrix] for i in range(len(matrix[0]))]

    # Get list of saddle point indices
    res = [[i+1,j+1] for i,x in enumerate(matrix) for j,y in enumerate(x) if y == max(x) and y == min(matrixT[j])]
    
    # Define Dictionary keys
    keys = ['row','column']
    
    return [dict(zip(keys,row)) for row in res]

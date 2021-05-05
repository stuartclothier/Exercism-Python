def classify(number):

    if number < 1:
        raise ValueError("Input number error.")
    
    # Generate list of possible factors
    List = list(range(1,int(number**0.5)+1))

    # Check for actual factors and save to set
    factors = set(factor for i in List if number % i == 0 
                for factor in (i, number//i))

    # Get aliquot sum value
    aliquotSum = sum(factors) - number


    if aliquotSum == number:
        aliquot = "perfect"
    elif aliquotSum < number:
        aliquot = "deficient"
    else:
        aliquot = "abundant"

    return aliquot
def slices(series, length):
    if 1 <= length <= len(series):
        return [series[i:i+length] for i in range(len(series)-
    length+1)]  
    else:
        raise ValueError('You deserve what you get')

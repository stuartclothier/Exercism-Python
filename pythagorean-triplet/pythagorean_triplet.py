def triplets_with_sum(n):
     
    trip = []
    for a in range(n//3-1, 2, -1):
        b = n*(n-2*a) // (2*(n-a))
        c = n - a - b
        if a<b and a*a + b*b == c*c:
            trip.append([a,b,c]); 
    return trip

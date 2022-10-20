def resetValuesInPlace(L, threshold):
    """If the value in the list is less than the given number, it returns 0"""
    for e in range(0,len(L)):
        if L[e] > threshold:
            L[e] = 0
    return L

            
            
        
    

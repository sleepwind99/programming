def resetValues(L, threshold):
    """Copy list L to the result and modify the result to fit the given condition."""
    Result = L[:]
    for e in range(0,len(L)):
        if Result[e] > threshold:
            Result[e] = 0
    return Result

            

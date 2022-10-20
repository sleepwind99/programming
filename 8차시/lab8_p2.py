def removeValuesInPlace(L, threshold):
    """When the value of the list is less than the given value, remove it."""
    ul = L[:]
    for e in ul:
        if e > threshold:
            L.remove(e)
    L = ul
    return L

def modCount(n,m):
    
    """user input m,n This program divide m to n~1 so we find amount of rest=0"""
    
    count = 0
    while m<=n and n>1:
        if n%m==0:
            count += 1
        n = n - 1
    return count
print(modCount(36,8))
    

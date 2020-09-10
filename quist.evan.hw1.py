
def awesum(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (1/i)
    return sum

def recursum(n):
    if n == 1:
        return 1
    else:
        sum = recursum(n-1) + (1/n)
    return sum

def whatsum(B):
    sum = 0
    count = 0
    while sum < B:
        sum = sum + (1/(count+1))
        count = count + 1
    return count

def recurchoose(n, k):
    if n == k:
        return 1
    elif k == 0:
        return 1
    else:
        sum = recurchoose(n-1, k) + recurchoose(n-1, k-1)    
    return sum
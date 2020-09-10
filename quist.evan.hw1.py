
def awesum(n):
    sum = 0 #Initialize Tracking Variable
    for i in range(1,n+1):
        sum = sum + (1/i)
    return sum

def recursum(n):
    if n == 1: #Base case
        return 1
    else:
        sum = recursum(n-1) + (1/n) #Call recursive function and add this case
    return sum

def whatsum(B):
    sum = 0 #Initialize Tracking Variables
    count = 0 
    while sum < B: #Check if sum > target value
        sum = sum + (1/(count+1)) #Add to the sum the amount of the current number
        count = count + 1 #Track the count
    return count

def recurchoose(n, k):
    if n == k: #Base case for when you have n choose n, which is always 1
        return 1
    elif k == 0: #Base case for when you are chosing 0 elements
        return 1
    else:
        sum = recurchoose(n-1, k) + recurchoose(n-1, k-1)    
    return sum
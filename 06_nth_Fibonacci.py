# def nthFibRec(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return nthFibRec(n - 1) + nthFibRec(n - 2)

def getNthFibMem(n, memoize = {1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFibMem(n-1,memoize) + getNthFibMem(n-2,memoize)
        return memoize[n]

# O(n) time | O(1) time
def getNthFib(n):
    lastTwo = [0,1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]
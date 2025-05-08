def max2(a,b):
    if a>b:
        return a
    else:
        return b
        
def max3(a,b,c):
    if max2(a,b) == a:
        return max2(a,c)
    else:
        return max2(b,c)
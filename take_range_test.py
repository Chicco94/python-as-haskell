def my_take(n,it):
    """Take the first n elements from an iterator"""
    idx = 0
    while idx < n:
        yield next(it)
        idx += 1

def my_range(start=0, end=-1, step=1):
    """extension of range...here you can build an infinite generator"""
    idx = start
    while idx != end:
        yield idx
        idx += step

# The problem is...which is the smallest number such that:
#   2a+1=k
#   3b+1=k
#   4c+1=k
#   5d+1=k
#   6e+1=k
#   7f  =k
#
# here the solution in python using the functions above
#
print(list(my_take(1,(x for x in my_range(1) if x%2==1 and x%3==1 and x%4==1 and x%5==1 and x%6==1 and x%7==0))))


# here the Haskell version
# take n [x | x <-[1..] , mod x 2 == 1, mod x 3 == 1, mod x 4 == 1, mod x 5 == 1, mod x 6 == 1, mod x 7 == 0]
#

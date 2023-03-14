# -------------------------------------- Task 1 -----------------------------------
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mult(x, y):
    return x * y

def exp(x, y):
    return x ** y

# TODO: Add definitions of sub(), div(), mult(), exp(), as well as neg() and sqrt().
#       neg() should return the negation of the given number, and sqrt() should
#       return the square root of the given number. 

def neg(x):
    return -1 * x # fill here

def sqrt(x):
    return x ** (1/2) # fill here

# -------------------------------------- Task 2 -----------------------------------

# TODO: Implement the quadratic formula using *only* the functions defined here.
#       Do not use arithmetic operators directly. 
#       You're allowed to define other functions.
a = 1
b = -3
c = 1

t1 = neg(b)
t2 = sqrt(sub(exp(b,2), mult(mult(4,a),c)))
t3 = mult(2, a)

x1 =  div(add(t1,t2), t3)# TODO: write a code to compute the first root of the quadratic equation
x2 = div(sub(t1,t2), t3) # TODO: then do the same for the second root
# Note: Make sure to remove the ellipsis (...) when you're writing your code

print("First root:" + str(x1))
print("Second root:" + str(x2))
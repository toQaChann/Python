import sympy

# Define the function f(x)
x = sympy.Symbol('x')
f_string = input("Enter the function f(x): ")
f = sympy.sympify(f_string)

# Set the interval [a, b]
a = float(input("Enter the left endpoint a: "))
b = float(input("Enter the right endpoint b: "))

# Set the estimated error
error_est = float(input("Enter the estimated error: "))

# Set the maximum number of iterations
max_iter = 1000

# Perform the bisection method
for i in range(max_iter):
    c = (a + b)/2
    fc = f.subs(x, c)
    if abs(fc) < error_est:
        break
    elif f.subs(x, a)*fc < 0:
        b = c
    else:
        a = c

# Print the solution or an error message
if i == max_iter-1:
    print("Failed to find solution within the maximum number of iterations.")
else:
    print("Solution: ", c)


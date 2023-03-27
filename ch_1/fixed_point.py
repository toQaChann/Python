import sympy

# Define the function g(x) = x - f(x)/f'(x)
x = sympy.Symbol('x')
f_string = input("Enter the function f(x): ")
f = sympy.sympify(f_string)
g = x - f/sympy.diff(f, x)

# Set the initial guess x0
x0 = float(input("Enter the initial guess x0: "))

# Set the estimated error
est_err = float(input("Enter the estimated error: "))

# Set the maximum number of iterations
max_iter = 1000

# Perform the fixed point iteration method
for i in range(max_iter):
    x_next = g.subs(x, x0)
    if abs(x_next - x0) < est_err:
        break
    x0 = x_next

# Print the solution or an error message
if i == max_iter-1:
    print("Failed to find solution within the maximum number of iterations.")
else:
    print("The solution is: ", x_next)


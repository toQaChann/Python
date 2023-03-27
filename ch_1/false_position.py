import sympy

# Define the function f(x)
x = sympy.Symbol('x')
f_string = input("Enter the function f(x): ")
f = sympy.sympify(f_string)

# Set the initial guesses x0 and x1
x0 = float(input("Enter the first initial guess x0: "))
x1 = float(input("Enter the second initial guess x1: "))

# Set the estimated error
est_err = float(input("Enter the estimated error: "))

# Set the maximum number of iterations
max_iter = 1000

# Perform the false position method
for i in range(max_iter):
    f0 = f.subs(x, x0)
    f1 = f.subs(x, x1)
    x_next = x1 - f1*(x1 - x0)/(f1 - f0)
    f_next = f.subs(x, x_next)
    if abs(f_next) < est_err:
        break
    elif f_next*f1 < 0:
        x0 = x1
        f0 = f1
    x1 = x_next

# Print the solution or an error message
if i == max_iter-1:
    print("Failed to find solution within the maximum number of iterations.")
else:
    print("The solution is: ", x_next)


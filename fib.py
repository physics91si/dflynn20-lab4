# Physics 91SI
# Spring 2015
# Lab 01
# Part 1
# Solution

<<<<<<< HEAD
import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        args = ["error"]
    if args[0] == "help":
        help_message = \
"""

fib.py

Usage
  - './fib.py approx n': display the n-th order Fibonacci approximation to
    the golden ratio.
  - './fib.py converge': keep calculating higher-order Fibonacci approximations
    to the golden ratio until it stops changing (to floating-point precision).
  - './fib.py help': display this help message.

"""
        print(help_message)
    elif args[0] == "approx" and len(args) == 2:
        phi_approx(int(args[1]))
    elif args[0] == "converge" and len(args) == 2:
	f = open(args[1],"w+")
	phi_converge(True, f)
    elif args[0] == "converge" and len(args) == 1:
	phi_converge(False)
    else:
        print("Error: input not understood.\n" \
                "    Type './fib.py help' for info on this program.")
=======
>>>>>>> parent of 7194f2a... Working version of fib.py
def fib(n):
    """Return nth element of the Fibonacci sequence."""
    # Create the base case
    n0 = 0
    n1 = 1
    
    # Loop n times. Just ignore the variable i.
    for i in range(n):
        n_new = n0 + n1
        n0 = n1
        n1 = n_new
    return n0

def phi_approx(n):
    """Return the nth-order Fibonacci approximation to the golden ratio."""
    fib_n = fibbb(n)
    fib_nm1 = fib(n - 1)
    phi = float(fib_n)/fib_nm1
<<<<<<< HEAD
    if show_output:
<<<<<<< HEAD
        phi_approx_output_format.format(n, fib_n, fib_nm1, phi)
=======
        print(phi_approx_output_format.format(n, fib_n, fib_nm1, phi))
>>>>>>> da89bd0a28746177a78a1d5414cfe221336fa64b
    return phi

phi_converge_output_format = \
"""Approximation order: {:d}
    phi_old: {:.25f}
    phi_new: {:.25f}"""

def phi_converge(file_present, f):
    """Keep calculating higher-order Fibonacci approximations to the golden
    ratio until it stops changing (to floating-point precision)."""

    i = 3
    phi_old = phi_approx(i - 1, show_output=False)
    phi_new = phi_approx(i, show_output=False)
    while phi_old != phi_new:
        i += 1
        phi_old = phi_new
        phi_new = phi_approx(i, show_output=False)
<<<<<<< HEAD
        if file_present:
	    f.write(phi_converge_output_format.format(i, phi_new, phi_old)+ "\n")
	else:
	    print phi_converge_output_format.format(i, phi_new, phi_old)
    
    if file_present:
	f.write("\nConverged to %.25f" % phi_new)
    else:
	print "\nConverged to %.25f" % phi_new

=======
        print(phi_converge_output_format.format(i, phi_new, phi_old))
    print("\nConverged to %.25f" % phi_new)
>>>>>>> da89bd0a28746177a78a1d5414cfe221336fa64b
if __name__ == '__main__': main()
=======
    print n, fib_n, fib_nm1, phi
    return phi

# Find successively better approximations
for i in range(2, 15):
    print phi_approx(i)
>>>>>>> parent of 7194f2a... Working version of fib.py

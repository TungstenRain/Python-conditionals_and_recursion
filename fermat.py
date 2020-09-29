"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    Copyright 2015 Allen B. Downey
    License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

    This is to test out the turtle module from Chapter 5: Conditionals and Recursion in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""

def check_fermat(a, b, c, n):
    """
        Check Fermat's theorem for validity
        'There are no positive integers a, b, and c such that 
            a**n + b**n = c**n
        for any values of n greater than 2

        a: integer
        b: integer
        c: integer
        n: integer
    """
    if n > 2:
        a_n = a**n
        b_n = b**n
        c_n = c**n
        a_n_b_n = a_n + b_n
        if (a_n_b_n == c_n):
            print("For integers a= " + str(a) + " b= " + str(b) + " c= " + str(c) + " and n= " + str(n) + ", Fermat's Theorem works!")
        else:
            print("For integers a= " + str(a) + " b= " + str(b) + " c= " + str(c) + " and n= " + str(n) + ", Fermat's Theorem is wrong!")
    else:
        print("n is not greater than 2")

def user_prompt():
    """
        Prompt the user for input to check Fermat's Theorem and then call the function to check the theorem.
    """
    print("We're going to check Fermat's Theorem that says there are no positive integers such that\n a^n + b^n = c^n \n for any values greater than 2.\n")
    a = int(input("Enter an integer for a: "))
    b = int(input("Enter an integer for b: "))
    c = int(input("Enter an integer for c: "))
    n = int(input("Enter an integer for n: "))
    check_fermat(a, b, c, n)

user_prompt()
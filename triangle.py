"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to test out the turtle module from Chapter 5: Conditionals and Recursion in Think Python 2
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""
def is_triangle(a, b, c):
    """
        Check to see if the three digits will make a triangle
        If any of the lengths is greater than the sum of the other two, then you cannot form a triangle.
        Otherwise, you can. If the sum of the two lengths equals the third, they form a "degenerate" triangle.

        a: integer
        b: integer
        c: integer
    """
    a_b = a + b
    a_c = a + c
    b_c = b + c
    if (a > b_c) or (b > a_c) or (c > a_b):
        print("For lengths a= " + str(a) + " b= " + str(b) + " c= " + str(c) + ", you cannot make a triangle.")
    elif (a == b_c) or (b == a_c) or (c == a_b):
        print("For lengths a= " + str(a) + " b= " + str(b) + " c= " + str(c) + ", you can make a degenerate triangle.")
    else:
        print("For lengths a= " + str(a) + " b= " + str(b) + " c= " + str(c) + ", you can make a triangle.")

def user_prompt():
    """
        Prompt the user for input to check lengths and then call the function to check lengths.
    """
    print("Checking stick lengths to see if we can make a triangle.\n")
    a = int(input("Enter the first stick length: "))
    b = int(input("Enter the second stick length: "))
    c = int(input("Enter the third stick length: "))

    is_triangle(a, b, c)

user_prompt()
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
import turtle


def draw_koch_curve(t, order, x):
    """
        Draw a Koch curve.

        t: Turtle
        order: the order of magnitude of the Koch curve
        x: integer length
    """
    if order == 0:
        t.forward(x)
    else:
        for angle in [60, -120, 60, 0]:
           draw_koch_curve(t, order-1, x/3)
           t.left(angle)

def draw_snowflake(t, order, x):
    """
        Draw a snowflake using three Koch curves

        t: Turtle
        x: integer length
    """
    for i in range(3):
        draw_koch_curve(t, order, x)
        t.rt(120)

def user_input():
    """
        Prompt user to input the length for the Koch curve
    """
    print("Welcome to drawing a Koch curve.\n")
    order = int(input("Please enter the order of magnitude for the Koch curve: "))
    x = int(input("Please enter a length x: "))
    # Instantiate the Turtle
    bob = turtle.Turtle()
    bob.hideturtle()
    draw_snowflake(bob, order, x)
    
# Call the user prompt
user_input()
turtle.mainloop()
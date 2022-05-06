"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_99()
        go_out()


def turn_right():
    for i in range(3):
        turn_left()


def turn_back():
    for i in range(2):
        turn_left()


def go_in():
    """
    pre-condition: Karel is at the upper left of the pothole, facing East.
    post-condition: Karel is in the pothole, facing South.
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition:Karel is in the pothole,facing South.
    post-condition:Karel is at the upper right of the pothole,facing East.
    """
    turn_back()
    move()
    turn_right()
    move()


def put_99():
    for i in range(99):
        put_beeper()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)

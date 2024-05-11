import os
import platform
import sys
import termios
import tty

use_logging = False

def _getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def print_line():
    print(
        "----------------------------------------------------------------------------------"
    )

def filter_array_by_id(list, id):
    for item in list:
        if item.id == id:
            return item

def any_key():
    print("Press any key to continue...")
    _getch()  # This will wait for a key press and capture the key stroke


def print_header():
    print_line()
    print("Meal Cost Calculator: CES-110 | Spring 2024")
    print("Developer: Johnathon D Smith")
    print_line()
    print()


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def print_title(title):
    print_line()
    print(title)
    print_line()


def print_top(title):
    clear_screen()
    print_header()
    print()
    print_title(title)
    print()


def universal_go_back():
    return ["Z", "z"]


def universal_quit():
    return ["Q", "q"]


def reserved_keys():
    start = universal_go_back()
    start.append(universal_quit())
    return start

def if_else(value, true_val, false_val):
    if value in ["Y", "y"]:
        return true_val
    else:
        return false_val
    
def get_input(prompt):
    return input(prompt)

def get_float_input(prompt):
    valid = False
    result = 0.0
    while not valid:
        try:
            result = float(input(prompt))
            valid = True
        except ValueError:
            print("Invalid Value... Try Again")
            any_key()
    return result

def get_int_input(prompt):
    valid = False
    result = 0
    while not valid:
        try:
            result = int(input(prompt))
            valid = True
        except ValueError:
            print("Invalid Value... Try Again")
            any_key()
    return result

def get_bool_input(prompt):
    valid = False
    result = False
    while not valid:
        value = input(prompt)
        if value in ["Y", "y"]:
            result = True
            valid = True
        elif value in ["N", "n"]:
            result = False
            valid = True
        else:
            print("Invalid Value... Try Again")
            any_key()
    return result

def log(message):
    if use_logging:
        print(f'LOG: {message}')
        any_key()



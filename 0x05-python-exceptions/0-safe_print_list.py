#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        my_list = [1, 2, x, g, z, 89]
        print(*my_list)

    except ListError:
        print("Sorry that element does not exist in the list")

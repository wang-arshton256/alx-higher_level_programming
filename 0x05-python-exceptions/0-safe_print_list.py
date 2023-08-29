#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    # Args:
    # mylist (list): The list of elements to print.
    # x (int): The number of elements of my_list to print.

    try:
        # Initialize a counter for the number of elemnts to be printed
        count = 0
        for i in my_list:
            if count < x:

                print("{}". format(my_list[count], end='')
                count += 1
        print()
     except IndexError:
        pass
        finally:
        # Return the number of elements printed
        return count

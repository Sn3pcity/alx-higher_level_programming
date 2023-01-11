#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for s in my_string:
        if s not in "cC":
            new_str += s
    return (new_str)

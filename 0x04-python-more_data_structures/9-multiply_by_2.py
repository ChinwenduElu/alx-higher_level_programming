#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dir_cpy = a_dictionary.copy()
    list_keys = list(dir_cpy.keys())

    for i in list_keys:
        dir_cpy[i] *= 2

    return (dir_cpy)

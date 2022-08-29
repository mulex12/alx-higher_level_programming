#!/usr/bin/python3
def no_c(my_string):
    remover = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            remover += i
            return (remover)

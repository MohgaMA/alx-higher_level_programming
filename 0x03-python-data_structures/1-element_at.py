#!/usr/bin/python3
def element_at(my_list, idx):
    l = len(my_list)
    if idx < 0 or idx > (l - 1):
        return(None)
    for i in range(l):
        if idx == i:
            return(my_list[i])

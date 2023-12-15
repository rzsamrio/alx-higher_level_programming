#!/usr/bin/python3
def remove_char_at(str, n):
    strcp = []
    for i in range(len(str)):
        if i == n:
            continue
        strcp.append(str[i])
    return "".join(strcp)

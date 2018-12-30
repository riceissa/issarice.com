#!/usr/bin/env python3

import sys
from urllib.parse import quote_plus

def main():
    with open(sys.argv[1], "r") as f:
        for line in f:
            print(tex_line(line.strip()))

def tex_line(line):
    state = "out"
    result = ""
    curr_math = ""
    # Each dollar sign toggles the state in and out of math
    for c in line:
        if state == "out" and c != "$":
            result += c
        elif state == "out" and c == "$":
            state = "in"
        elif state == "in" and c != "$":
            curr_math += c
        elif state == "in" and c == "$":
            state = "out"
            result += '''<img class="pluginslug" src="/plugin_helper.php?plugin=equation&amp;tex=%s" alt="" />''' % quote_plus(curr_math)
            curr_math = ""
    return result

if __name__ == "__main__":
    main()

# TODO do we need to wrap math with &nbsp; ?

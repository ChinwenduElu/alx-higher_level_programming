#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        outcome = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        outcome = None

    return (outcome)

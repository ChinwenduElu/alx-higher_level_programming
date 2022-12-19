#!/usr/bin/python3
def magic_calculation(a, b):
    outcome = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception("Too far")
            else:
                outcome += (a ** b) / i
        except:
            outcome = b + a
            break
    return (outcome)

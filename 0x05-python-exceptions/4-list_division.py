#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            outcome = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            outcome = 0
        except TypeError:
            print("wrong type")
            outcome = 0
        except IndexError:
            print("out of range")
            outcome = 0
        finally:
            new_list.append(outcome)

    return (new_list)

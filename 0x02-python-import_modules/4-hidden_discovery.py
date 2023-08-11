#!/usr/bin/python3
""" prints all the names defined by the compiled module hidden_4.pyc"""

if __name__ == "__main__":

    import hidden_4

    nme = dir(hidden_4)
    for name in nme:
        if name[:2] != "__":
            print(name)

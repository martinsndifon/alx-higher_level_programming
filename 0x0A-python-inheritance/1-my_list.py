#!/usr/bin/python3

"""My_List Module"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints list in sorted order"""

        print(sorted(self))

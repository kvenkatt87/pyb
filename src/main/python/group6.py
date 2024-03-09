"""
This is a simple module to demonstrate a hello world function in Python.
"""

import sys

def group6(out):
    """
    Print a message new

    Args:
        out: Output stream to write the message to.
    """

    out.write("Assignment Pending\n")

# Call the function with a file object
group6(sys.stdout)

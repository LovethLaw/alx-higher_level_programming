#!/usr/bin/python3
"""
    This Module That Indents a string
    Args:
        text(str): string to be indented
"""
def text_indentation(text):
    """
        This Function indent a string when it comes in contact with . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char,end="")
        if char in [".", "?", ":"]:
            print("\n\n", end="")

#!/usr/bin/python3
def text_indentation(text):
    """
        Prints a text with two new lines after each '.', '?' and ':'
    """
    if not isinstance(text, str):

        raise TypeError("text must be a string")

    new_line_chars = [".", "?", ":"]
    current_line = ""

    for char in text:

        current_line += char

        if char in new_line_chars:

            print(current_line.strip())
            print()
            current_line = ""

    if current_line:

        print(current_line.strip())

#!/usr/bin/python3
"""This Module That prints out the first name and last name
    Args:
        first_name(string): parameter first name
        last_name(string): parameter last_name
    """
def say_my_name(first_name, last_name=""):
    """This function prints out the first name and last name"""
    if not isinstance(first_name, str): 
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f"My name is {first_name} {last_name}")


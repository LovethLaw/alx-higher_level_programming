#!/usr/bin/python3
"""module contains class MyInt"""


class MyInt(int):
    """defines the MyInt class"""
    def __eq__(self, num):
        return (int(self) != int(num))

    def __ne__(self, num):
        return (int(self) == int(num))
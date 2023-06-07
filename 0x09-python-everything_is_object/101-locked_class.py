#!/usr/bin/python3
"""This module contains the class LocckdClass"""


class LockedClass():
    """ prevents the user from dynamically creating new instance attributes, \
        except if the new instance attribute is called first_name"""
    __slots__ = ["first_name"]

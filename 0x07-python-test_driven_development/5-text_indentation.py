#!/usr/bin/python3
"""
This module contains the text_indentation method
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after \
        eachof these characters: ".?:"

    Args:
        text (str): Must be a string.

    Raises:
        TypeError: If text is not str, raise TypeError exception \
            with the message 'text must be a string'
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end='\n\n')
            if i + 1 < len(text):
                while text[i + 1] == ' ':
                    i += 1
        else:
            print(text[i], end='')
        i += 1

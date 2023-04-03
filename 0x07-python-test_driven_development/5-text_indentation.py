#!/usr/bin/python3
"""prints a text with 2 lines after: ., ? and :"""
def text_indentation(text):
    """
    Function to print a text with 2 lines after: ., ? and :
    Args:
        text: only parameter
    Returns:
        void
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            print(text[i], end='')
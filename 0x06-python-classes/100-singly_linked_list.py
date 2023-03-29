#!/usr/bin/python3
"""Node class"""
class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Initializes the data"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter methods"""
        return self.__data

    @property
    def next_node(self):
        """getter methods"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """setter methods"""
        if type(value) is not int:
            raise TypeError("Data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """setter methods"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

"""SinglyLinkedList"""
class SinglyLinkedList:
    """SinglyLinkedList class"""
    def __init__(self):
        """Initializes the data"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """returns the list"""
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]

"""
Module for methods that generate arrays.
"""
import random


def random_array(len_arr):
    """
    Function generates an array of size 2 ** n of random integers.
    """
    array = []
    for _ in range(len_arr):
        array.append(random.randint((-10)**5, 10**5))
    return array

def sorted_array(len_arr):
    """
    Function generates a sorted array of size 2 ** n.
    """
    array = []
    for i in range(len_arr):
        array.append(i)
    return array

def backward_sorted_array(len_arr):
    """
    Function generates a backward array of size 2 ** n of integers.
    """
    array = []
    for i in range(len_arr):
        array.append(len_arr-i)
    return array


def set_array(len_arr):
    """
    Function generates an array of size 2 ** n of repeated {1,2,3} elements.
    """
    array = []
    for _ in range(len_arr):
        array.append(random.randint(1,3))
    return array
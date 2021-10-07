"""
Module for experiments.
"""
import random
import json
from json import *
from alghoritms import *
import time
from pprint import pprint
from array_generation import *
# import matplotlib as plt
# plt.show()


results = {
    "random_array_time": {
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },

    "random_array_comparisons":{
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },

    "sorted_array_time": {
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },

    "sorted_array_comparisons":{
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },
    "backward_sorted_array_time": {
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },
    "backward_sorted_array_comparisons":{
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },
    "set_array_time": {
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },
    "set_array_comparisons":{
        "selection_sort": [],
        "insertion_sort":[],
        "merge_sort":[],
        "shell_sort":[],
    },
}

def test():
    """
    Function tests the algorithms of selection sort, insertion sort,
    merge sort and shell sort.
    Run the experiment for all the 4 sorting algos and 8 types of inputs.
    """
    test_random_array(results)
    test_sorted_array(results)
    test_backward_sorted_array(results)
    test_set_array(results)


def test_random_array(data):
    """
    Test the algos for random arrays of size 2^7 - 2^15.
    Testing 5 times and getting the average time and number of comparisons.
    Writes to a dictionary.
    """
    for n in range(7, 16):
        for algoritm in (selection_sort, insertion_sort, merge_sort, shell_sort):

            for j in range(5):
                time_f = 0
                comp_f = 0

                array = random_array(2 ** n)
                start = time.time()
                result = algoritm(array)

                work_time = time.time() - start
                time_f += work_time
                comp = result[1]
                comp_f += comp
            data["random_array_time"]["{}".format(algoritm.__name__)].append(time_f/5)
            data["random_array_comparisons"]["{}".format(algoritm.__name__)].append(comp_f/5)

            

def test_sorted_array(data):
    """
    Test the algos for a sorted array of elements of size 2^7 - 2^15..
    Writes to a dictionary.
    """
    for n in range(7, 16):
        for algoritm in (selection_sort, insertion_sort, merge_sort, shell_sort):

            array = sorted_array(2 ** n)
            start = time.time()
            result = algoritm(array)

            work_time = time.time() - start
            comp = result[1]
            data["sorted_array_time"]["{}".format(algoritm.__name__)].append(work_time)
            data["sorted_array_comparisons"]["{}".format(algoritm.__name__)].append(comp)

def test_backward_sorted_array(data):
    """
    Test the algos for sorted inverse array elements of size 2^7 - 2^15.
    Testing 1 time and getting the average time and number of comparisons.
    Writes to a dictionary.
    """
    for n in range(7, 16):
        for algoritm in (selection_sort, insertion_sort, merge_sort, shell_sort):
            array = backward_sorted_array(2 ** n)
            start = time.time()
            result = algoritm(array)

            work_time = time.time() - start
            comp = result[1]
            data["backward_sorted_array_time"]["{}".format(algoritm.__name__)].append(work_time)
            data["backward_sorted_array_comparisons"]["{}".format(algoritm.__name__)].append(comp)

def test_set_array(data):
    """
    Test the algos for arrays of {1, 2, 3} elems. of size 2^7 - 2^15.
    Testing 3 times and getting the average time and number of comparisons.
    Writes to a dictionary.
    """
    for n in range(7, 16):
        for algoritm in (selection_sort, insertion_sort, merge_sort, shell_sort):
            for j in range(3):
                time_f = 0
                comp_f = 0
                array = random_array(2 ** n)
                start = time.time()
                result = algoritm(array)

                work_time = time.time() - start
                time_f += work_time
                comp = result[1]
                comp_f += comp
            data["set_array_time"]["{}".format(algoritm.__name__)].append(time_f/3)
            data["set_array_comparisons"]["{}".format(algoritm.__name__)].append(comp_f/3)


if __name__ == '__main__':
    test()
    with open("final_results.json", "w") as f:
        f.write(dumps(results, indent=4))
    pprint(results)

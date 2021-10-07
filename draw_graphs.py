"""
Module that draws graphs.
"""
from json import *
import json
import matplotlib.pyplot as plt

def read_json(path):
    """
    Read the json file from the path and turn it into dict.
    Return the data
    """
    with open(path, "r") as file:
        data = json.load(file)

    return data


graph = {"random_array_time": 
            ["Time taken", "Randomly generated Array | Time"],
        "random_array_comparisons": 
            ["Number of comparisons", "Randomly generated Array | Changes"],
        "sorted_array_time": 
            ["Time taken", "Sorted Array | Time"],
        "sorted_array_comparisons": 
            ["Number of comparisons", "Sorted Array | Changes"],
        "backward_sorted_array_time": 
            ["Time taken", "backward sorted Array | Time"],
        "backward_sorted_array_comparisons": 
            ["Number of comparisons", "backward sorted Array | Changes"],
        "set_array_time": 
            ["Time taken", "{1, 2, 3} set Array | Time"],
        "set_array_comparisons": 
            ["Number of comparisons", "{1, 2, 3} set Array | Time"]}

data = read_json('final_results.json')

def create_graph():
    """
    Generates all the required graphs.
    """
    arrays = list(graph.keys())
    experiment = 1
    for array in arrays:
        figure, ax = plt.subplots()
        ax.set_yscale('log')
        for sorting in list(data[array].keys()):
            x = data[array][sorting]
            y = ["2^7", "2^8", "2^9", "2^10",
                 "2^11", "2^12", "2^13", "2^14", "2^15"]
            plt.plot(y, x, label=sorting.replace("_sort", ""))
        ax.set(xlabel='|Array length|', ylabel=graph[array][0], title=graph[array][1])
        ax.grid()
        ax.legend()
        plt.show()
        experiment += 1


if __name__ == '__main__':
    create_graph()

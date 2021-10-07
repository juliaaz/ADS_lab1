"""
Module which implements different sorts of an array of n elements.
"""
import time

def selection_sort(lst):
    '''
    lst -> (lst, int)
    Performs sorting by selection method.
    Returns sorted array and number of comparisons made.
    :param lst: list to be sorted.
    :return: sorted lst and number of comparisons.
    '''
    sel_counter = 0
    length = len(lst)
    for i in range(length):
        minn_i = i
        for key in range(i+1, length):
            sel_counter += 1
            if lst[minn_i] > lst[key]:
                minn_i = key
        lst[i], lst[minn_i] = lst[minn_i], lst[i]
    return lst, sel_counter

def insertion_sort(lst):
    '''
    lst -> (lst, int)
    Performs sorting by insertion method.
    Returns sorted array and number of comparisons made.
    :param lst: list to be sorted.
    :return: sorted lst and number of comparisons.
    '''
    ins_counter = 0
    for i in range(1, len(lst)):
        key = lst[i]
        flag = i - 1
        ins_counter += 1
        while flag > -1 and lst[flag] > key:
            ins_counter += 1
            lst[flag + 1] = lst[flag]
            flag -= 1
        lst[flag + 1] = key
    return lst, ins_counter


def shell_sort(lst):
    '''
    lst -> (lst, int)
    Performs sorting by shell method.
    Returns sorted array and number of comparisons made.
    :param lst: list to be sorted.
    :return: sorted lst and number of comparisons.
    '''
    she_counter = 0
    length = len(lst)
    gap = length // 2
    while gap:
        for i in range(gap, length):
            element = lst[i]
            flag = i
            she_counter += 1
            while flag > gap-1 and lst[flag - gap] > element:
                she_counter += 1
                lst[flag] = lst[flag - gap]
                flag -= gap
            lst[flag] = element
        gap //= 2
    return lst, she_counter


def merge_sort(lst):
    '''
    lst -> (lst, int)
    Performs sorting by merge method.
    Returns sorted array and number of comparisons made.
    :param lst: list to be sorted.
    :return: sorted lst and number of comparisons.
    '''
    mer_counter = 0
    length = len(lst)
    if length <= 1:
        return lst, mer_counter

    middle = length//2
    left_part, right_part = lst[:middle], lst[middle:]

    res_left = merge_sort(left_part)
    left_part = res_left[0]

    res_right = merge_sort(right_part)
    right_part = res_right[0]

    mer_counter += res_left[1] + res_right[1]
    left_part.append(float('inf'))
    right_part.append(float('inf'))

    idx_left, idx_right = 0, 0
    for i in range(length):
        if right_part[idx_right] < left_part[idx_left]:
           lst[i] = right_part[idx_right]
           idx_right += 1
        else:
            lst[i] = left_part[idx_left] 
            idx_left += 1
        mer_counter += 1
    
    return lst, mer_counter

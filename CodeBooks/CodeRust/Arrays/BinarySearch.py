#!/usr/bin/env python3

def binary_search_rec(array, item):
    '''
    Implement recursive binary search for sorted array
    return index when get the value
    return -1 when not in array
    '''
    if len(array)==0:
        return -1
    high = len(array) - 1
    def binary_search(low, high):
        mid = (high + low)/2
        if array[mid] == item:
            return mid
        elif array[low] <= item < array[mid]:
            high = mid - 1
        elif array[mid] < item <= array[high]:
            low = mid + 1
        else:
            return -1
        return binary_search(low, high)
    return binary_search(0, high)


def binary_search_iter(array, item):
    '''
    Implement iterative binary search for sorted array
    return index when get the value
    return -1 when not in array
    '''
    high = len(array) - 1
    low = 0
    while high >= low:
        mid = (high + low)/2
        if array[mid] == item:
            return mid
        elif array[low] <= item < array[mid]:
            high = mid - 1
        elif array[mid] < item <= array[high]:
            low = mid + 1
        else:
            return -1
    else:
        return -1



if __name__ == '__main__':
    array = [1, 10, 20, 47, 59, 63, 75, 88, 99]
    assert -1==binary_search_rec([], 0)
    assert -1==binary_search_rec(array, 100)
    assert 3==binary_search_rec(array, 47)
    assert 8==binary_search_rec(array, 99)
    assert 0==binary_search_rec(array, 1)

    assert -1==binary_search_iter([], 0)
    assert -1==binary_search_iter(array, 100)
    assert 3==binary_search_iter(array, 47)
    assert 8==binary_search_iter(array, 99)
    assert 0==binary_search_iter(array, 1)

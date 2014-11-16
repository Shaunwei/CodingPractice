#!/usr/bin/env python3

def binary_search_rec(a, key):
    def binary_search(a, key, low, high):
        if low > high:
            return -1

        mid = (low + high) / 2
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            return binary_search(a, key, low, mid - 1)
        else:
            return binary_search(a, key, mid + 1, high)
    return binary_search(a, key, 0, len(a) - 1)

def binary_search_iter(a, key):
    low = 0
    high = len(a) - 1
    while low <= high:  #need to be <= not <, value could be same
        mid = (low + high) / 2
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
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
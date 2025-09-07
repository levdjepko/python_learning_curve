def maxMin(k, arr):
    
    # find the difference between the min and max elements of the array
    # such that its smallest and largest elements are as close as possible
    arr.sort()
    max_difference = arr[len(arr) - 1] - arr[0]
    for i in range(len(arr) - k + 1):
        min_element = arr[i]
        max_element = arr[i + k - 1]
        difference = max_element - min_element
        if difference < max_difference:
            max_difference = difference
    return max_difference

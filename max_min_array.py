def maxMin(k, arr):
    
    # create an array of length k from arr
    # such that its smallest and largest elements are as close as possible
    
    arr.sort()
    max_difference = arr[len(arr) - 1] - arr[0]
    for i in range(len(arr) - k + 1):
        # new_array = arr[i : i + k]
        # print ("new array:", arr[i : i + k])
        min_element = arr[i]
        max_element = arr[i + k - 1]
        difference = max_element - min_element
        if difference < max_difference:
            max_difference = difference
    return max_difference

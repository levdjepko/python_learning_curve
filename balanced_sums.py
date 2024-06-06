def balancedSums(arr):
    # find an element in the array such that sum of elements to the left and to the right equals
    # if that's the case, return 'yes', otherwise 'no'
    sum_of_all_elements = sum(arr)
    if len(arr) == 1:
        return 'YES'
    left = 0
    right = sum_of_all_elements
    for i in range(len(arr)):
        # track the sum before and after the current element
        if i >= 1:
            left += arr[i - 1]
        right -= arr[i]
        if left == right:
            return 'YES'
    return 'NO'

def minimumAbsoluteDifference(arr):
    arr.sort() 
    min_diff = arr[len(arr) - 1] - arr[0]
    for i in range(len(arr) - 1):
         if arr[i + 1] - arr[i] <= min_diff:
             min_diff = arr[i + 1] - arr[i]
    return min_diff        

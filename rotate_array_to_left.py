
def rotateLeft(d, arr):
    new_array = []
    
    for i in range(d, len(arr)):
        new_array.append(arr[i])
    for i in range(0, d):
        new_array.append(arr[i])
    return new_array        

def gamingArray(arr):
    # find the max element in the array and remove everything to the right of it
    # OPTIMIZED FOR EFFICIENCY
    pick_counter = 0
    max_element = 0
    
    for i in range(len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
            pick_counter += 1
    if (pick_counter % 2 == 1):
        return 'BOB'
    else:
        return 'ANDY'  

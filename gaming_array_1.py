def gamingArray(arr):
    # find the max element in the array and remove everything to the right of it
    #print ("*** New task")
    #print (arr)
    pick_counter = 0
    while(len(arr) >= 1):
        pick_counter += 1
        if (pick_counter % 2 == 1):
            print("BOB:")
        else:
            print("ANDY:")    
        index_max = max(range(len(arr)), key=arr.__getitem__)
        #print(index_max)
        #print("Removing array:", arr[index_max:])
        arr = arr[:index_max]
        #print ("Remaining array:", arr)
    if (pick_counter % 2 == 1):
        return 'BOB'
    else:
        return 'ANDY'    

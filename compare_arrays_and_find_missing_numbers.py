def missingNumbers(arr, brr):
    # return the nnumbers missing in one of the arrays
    missing_items = []
    arr.sort()
    brr.sort()    
    index = 0
    
    for i in range(len(brr)):
        if brr[i] == arr[index]:
            index += 1
        else:
            if brr[i] not in missing_items:
                # append the item, we haven't tracked it yet
                missing_items.append(brr[i])
    return missing_items   

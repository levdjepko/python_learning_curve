def minimumBribes(q):
    
    bribes = 0
    reference_array = list(range(1, n+1))
    
    for i in range(len(q)-1):
        if q[i] != reference_array[i]:
            # Swap
            reference_array[i], reference_array[i+1] = reference_array[i+1], reference_array[i]
            if q[i] != reference_array[i]:
                # Swap again
                reference_array[i], reference_array[i+2] = reference_array[i+2], reference_array[i]
                if q[i] == reference_array[i]:
                    bribes += 2
                else:
                    print('Too chaotic')
                    return
            else:
                bribes += 1
    print(bribes)
    return

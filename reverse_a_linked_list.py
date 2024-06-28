def reverse(llist):
    # reverse a linked list
    previous_node = None
    while llist:
        # store a pointer to the next node in a temporary variable
        temp_node = llist.next
        # set the pointer to the previous node
        llist.next = previous_node
        # update the previous node with current one
        previous_node = llist
        # move the head
        llist = temp_node
    return previous_node
        

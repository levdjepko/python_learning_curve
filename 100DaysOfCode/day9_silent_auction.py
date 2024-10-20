
bids_dict = {}
next = 'initial'
max_bid = -1
max_bidder = ""
while (next == 'yes' or next == 'initial'):
    # print("\n" * 30)
    bidder = input("What is your name? ")
    price = int(input("What is your bid? "))
    next = input("Are there other bidders? yes or no: ")

    bids_dict[bidder] = price
    if price > max_bid:
        max_bid = price
        max_bidder = bidder
    #print(bids_dict)

# TODO-4: Compare bids in dictionary
print(f"Max bidder is {max_bidder} with a bid of {max_bid}")



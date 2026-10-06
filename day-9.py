bids = {}
again = True
while again:
    name = input("What is your name?\n")
    bid = int(input("How much do you want to bid?\n$ "))
    bids[name] = bid

    users = input("Are there any more bidders?\n")
    if users == "no":
        again = False

highest_bid = 0
for bidder in bids:
    bid_money = bids[bidder]
    if bid_money > highest_bid:
        highest_bid = bid_money
        winner = bidder

print(f"The winner is {winner} with a bid amount of ${highest_bid}.")
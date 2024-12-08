def winner(bidders):
    number =0
    win = ''
    for i in bidders:
       bidder_details = bidders[i]
       if bidder_details>number:
           number = bidder_details
           win = i
    print(f'The winner is {win} with bid price of {number}')
       
bidder ={}   
end_bidding = False
while not end_bidding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid price: "))
    bidder[name]=price
    more_bidder = input("Enter yes for more bidder or no for exist: ").lower()
    if more_bidder == 'no':
        end_bidding = True
winner(bidders=bidder)

    
    
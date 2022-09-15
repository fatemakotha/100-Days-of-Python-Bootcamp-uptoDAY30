

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record): # bidding_record = {"Angela": 123, "James": 321}
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record: #bidder is "Angela", then bidder is "James"
  #for "Angela" in {"Angela": 123, "James": 321}:
    bid_amount = bidding_record[bidder] #bid amount is a new variable set to the value of the KEY "Angela" which is 123
   #bid_amount = {"Angela": 123, "James": 321}[Angela]
   #bid_amount = 123
    if bid_amount > highest_bid: 
     #bid_amount > 0 #if this is true
      highest_bid = bid_amount
      #highest_bid = 123
      winner = bidder #bidder here in "Angela"
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished: #.......................1
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price#Adding the KEY: name and VALUE: price to bids{} DICTIONARY
  print(bids) #prints: {'kotha': 90, 'cutu': 888}
  
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)#Passes the DIC bids through find_highest_bidder()
   #find_highest_bidder({"Angela": 123, "James": 321})    
    
  elif should_continue == "yes":
    print("Carry on") #keeps LOOPING through the WHILE loop to ask for more KEYS and VALUES to the Dictionary named bids
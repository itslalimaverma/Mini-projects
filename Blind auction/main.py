from replit import clear
from art import logo
print(logo)

print("This is a silent auction program.")
print("Please enter your name and your bids!")
bidding_finished = False
auction_dict={}

def find_highest_bidder(auction_dict):
  highest_bid = 0
  highest_bidder = ""
  for bidder in auction_dict:
    if auction_dict[bidder] > highest_bid:
      highest_bid = auction_dict[bidder]
      highest_bidder = bidder
  return highest_bidder
  
while not bidding_finished:
  name=input("Enter your name: ")
  bid=int(input("Enter your bid:$"))
  auction_dict[name]=bid
  more=input("Are there any other bidders? Type 'yes' or 'no'.")
  if more=="no":
    bidding_finished=True
    break
  elif more=="yes":
    clear()
  else:
    print("Please enter 'yes' or 'no'.")
    continue

result=find_highest_bidder(auction_dict)
print(f"The winner is {result} with a bid of ${auction_dict[result]}.")


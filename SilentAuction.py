# Dictionaries in python
# {"key":"value"}
# programming_dictionary = {
#     "Bug":"something",
#     "function": "another thing",
# }

# Retrieving data from dictionary
# print(programming_dictionary["Loop"])

# Adding new entry
# programming_dictionary["Loop"] = "Third thing"

# Creating an empty dictionary
# empty_dic = {}

# wipw an existing dictionary
# programming_dictionary = {}

# Loop through dictionary
# for key in programming_dictionary:
    # print(key)
    # print(programming_dictionary[key])***** to print value of respecitve key******


# Silent Aucution

import os

print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False



def find_highest(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bidding_price = bidding_record[bidder]   
    if bidding_price > highest_bid:
      highest_bid = bidding_price
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid} ")   

while not bidding_finished:

  name = input("What is your name?: " )
  bid = int(input("What's your bid?:"))
  bids[name] = bid
  more = input("Are there any other biders? Type 'yes' or 'no'")
  if more == "no":
    bidding_finished = True
    find_highest(bids)
  elif more == "yes":
    os.system('cls')  


       



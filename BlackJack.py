#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#    https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt



#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 
# 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21,
#  remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List.
#  If no, then the game has ended.
#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, 
# then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. 
# If the computer_score is over 21, then the computer loses. 
# If none of the above, then the player with the highest score wins.
import random 
import os


def deal_card():
     """Return  arandom card from the deck"""
     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
     return random.choice(cards) 

def calculate_score(cards):
     """Calculates total sum of the card in the list"""

     if sum(cards ) == 21 and len(cards ) == 2:
          return 0 
     if 11 in cards and sum(cards) > 21:
        #   card_list[card_list.index(11)] = 1
          cards.remove(11)
          cards.append(1)
          
     return sum(cards) 

def compare(user_score,computer_score):
     if user_score == computer_score:
         return "It's Draw"
     elif computer_score == 0:
          return "You loose"
     elif user_score == 0:
          return "You win" 
     elif user_score > 21:
          return "You loose"
     elif computer_score > 21:
          return "You win" 
     elif user_score > computer_score:
          return "You win"
     elif computer_score > user_score:
          return " Opponents score is greater than you.You loose"
     

def play_game():     
                   
    
    user_cards = []
    computer_cards = []

    game_is_on = True



        

    for _ in range(0,2):
        card = deal_card()
        user_cards.append(card)
        
    for _ in range(2):
        card = deal_card()
        computer_cards.append(card)

    while game_is_on:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card {user_cards} and score: {user_score}")
        print(f"Computer's first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_on = False
        else:

            another_card =  input("Type 'y' to get another card, type 'n' to pass ")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_is_on = False  


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))     

while input("DO you want to play game of Blackjack? Type 'y' or'n' :") == "y":
     os.system('cls')
     play_game()


          
    
     


     

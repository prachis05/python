print('''
                                 _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''' )




print("Welcome to tresure Island")
print("Your mission is to find tresure")
left_or_right = input('You are at the crossroad . where do you want to go ? Type "left" or "right"')
if left_or_right == "left":
    wait_or_swim = input("You came to a lake.There is an island in the middle of the lake Type 'wait' to wait for a boat . type swim to swim across")
    if wait_or_swim == "wait":
        which_colour = input("You arrive at the island unbarred There is a house with 3 doors. One red,one yellow and one blue.Which colour do you choose?")
        if which_colour == "red":
            print("Ooops snakes")
        elif which_colour == "blue":
            print("Yayyyyy you got luck")
        else:
            print("Beastsss")        
    else:
        print("Oooopss you LOST")
else:
    print("Ooopss you LOST")    


  


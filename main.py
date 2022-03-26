'''
This is the game of Black Jack.
You start off with 50 coins and before the game begins, the player decides on how much to bet.
The player only has the option to hit or stand. No other options are avialable

if the player beats the dealer then the player gets their bet back times 2
if the player ties the dealer then the player gets their bet back
if the player hits black jack and wins they get 3 times their bet back
if the player loses then they lose their bet

'''


import GameMechanics
import os
import time

'''
The printHands functin prints the cards that both the Dealer
and the Player have. By default turn will equal D which stands for Dealer.
You can optionaly pass in P which means its the players turn.
If it's the players turn, only the first card of the dealer is shown and 
the second card is hidden. 
'''
def printHands(Dealer,Player,turn='D'):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print ("Dealers Hand") 
    if turn == "P":
        print (Dealer.cards[0])
        print (f"Deals hand equals {Dealer.getHalfValue()} plus the value of 1 other hidden card")
    else:
        for card in Dealer.cards:
            print (card)
        print (f"Deals hand equals {Dealer.value}")
    print ("\n")
    print ("\n")
    print ("Players Hand")
    for card in Player.cards:
        print (card)
    if Player.value == 21:
        print (f"Players hand equals {Player.value} BLACK JACK!")
    else:
        print (f"Players hand equals {Player.value}")
    print ("\n")


if __name__ == "__main__":
    Player = GameMechanics.PlayerHand()
    Dealer = GameMechanics.DealerHand()
    
    
    MainDeck = GameMechanics.Deck()
    
    playerContinue = True
    
    #Loop that continues a brand new game
    while playerContinue:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #reset the deck and deals out the Player and Dealers initial hands
        MainDeck.setDeck()
        Dealer.AddCard(MainDeck.cards.pop(0))
        Dealer.AddCard(MainDeck.cards.pop(0))
        Dealer.setHalfValue(Dealer.cards[0])
    
        Player.AddCard(MainDeck.cards.pop(0))
        Player.AddCard(MainDeck.cards.pop(0))
        
        #Asks the player how much they want to bet for the upcoming game
        getBet = True
        while getBet:
            try:
                bet = int(input(f"You have {Player.coins} coins. How much would you like to bet? "))
            except:
                print ("Invalid bet. Try again.")
                continue
            if bet > Player.coins:
                print("Sorry. You don't have that much to bet")
            elif bet <= 0:
                print("Sorry. You have to bet a postive amount of coins")
            else:
                getBet = False
        Player.coins -= bet     
        
        #This loop continues the players turn until they decide to Stand
        PlayersTurn = True
        while PlayersTurn:
            printHands(Dealer,Player,'P')
            action = input("Do you want to Hit or Stand? H/S ")
            if action != "H" and action != "S":
                print("Invalid option. Try again. Please type H or S")
                continue
            if action == "H":
                Player.AddCard(MainDeck.cards.pop(0))
                if Player.value > 21:
                    print ("You went bust")
                    PlayersTurn = False
                elif Player.value == 21:
                    print("You got 21 points! BLACK JACK!!!")
                    PlayersTurn = False
            else:
                PlayersTurn = False
        
        #This loop continues the Dealers turn until they win, lose, or tie.
        while Dealer.value < 22 and Player.value < 22 and Dealer.value < Player.value:
            printHands(Dealer,Player)
            print ("Dealer draws new card ...")
            time.sleep(2)
            Dealer.AddCard(MainDeck.cards.pop(0))
        
        printHands(Dealer,Player)
        
        #determine if the player has won. The program assumes the Player loses until proven otherwise
        PlayerWon = False
        if Player.value <= 21:
            if Dealer.value > 21:
                PlayerWon = True
            elif Player.value > Dealer.value:
                PlayerWon = True
        
        #Prints out if the Player has won, lost, or ties and assigns coins appropriately
        if PlayerWon:
            if Player.value != 21:
                print(f"You won!. Congrats you have won {bet * 2} coins!")
                Player.addCoins(bet * 2)
            else:
                print(f"for getting Black Jack, you now get 3 times your bet.")
                print(f"Congrats. You have won {bet * 3} coins!")
                Player.addCoins(bet * 3)
        elif Dealer.value == Player.value:
            print(f"It was tie. You get your bet back")
            Player.addCoins(bet)
        elif not PlayerWon:
            print(f"Sorry. Dealer has won.")
        print(f"You now have {Player.coins} coins")
        
        #If the player has coins over 0 then the program asks if they want to play again
        #If the player run out of coins then the game is over
        if Player.coins != 0 :
            getInput = True
            while getInput:
                playAgain = input("Would you like to play again? Y/N ")   
                if playAgain != "Y" and playAgain != "N":
                    print("Invalid input. Please type Y or N")
                    continue
                else:
                    getInput = False
            if playAgain == "N":
                playerContinue = False
            else:
                Player.ClearCards()
                Dealer.ClearCards()
        else:
            print("Sorry. You are out of coins. Game Over")
            playerContinue = False
           
            
        
            
            




         
                
        
             
        




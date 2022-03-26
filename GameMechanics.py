import random

#Global varriables for all cards in a standard deck
SUITS = ("Hearts","Spades", "Clubs", "Diamods")

NUMBERS = {"Two" : 2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, 
    "Eight":8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, 
    "King": 10, "Ace": 11}

'''
The class is for each card in the game. Determines Suite, number of 2 through Ace, and the value
of that card in the game of black jack. 
By default Aces is given the value of 11, but the actual value is determined later in the Hand class
This class also determins how to print each card
'''
class Card():
    
    def __init__(self, suit, number):
        
        self.suit = suit
        self.number = number
        self.value = NUMBERS[number]
        
        
    def __str__(self):

        return "**" + self.number + " of " + self.suit + "**"
    
    
'''
This class has all 52 cards in it. the setDeck() method resets the deck
and shuffles it. The setDeck will get called each time the player wants to
play a new game of Black Jack

'''
class Deck():
    
    def __init__(self):
        self.cards = []
        
    def setDeck(self):
        self.cards.clear()
        for suit in SUITS:
            for number in NUMBERS.keys():
                self.cards.append(Card(suit,number))
        random.shuffle(self.cards)


'''
This is the base class for the player and dealer hands
When you call the AddCard method it adds the card you pass
to it. Then it determines its value and adds that to the total
value of the hand. It also determines if the Ace card
is worth 1 or 11 points

ClearCards is called when the player decides to play a new game of Black Jack
'''        
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def AddCard(self, card):
        numberOfAce = 0
        self.cards.append(card)
        self.value = 0
        
        for card in self.cards:
            if card.number == "Ace":
                numberOfAce += 1
            else:
                self.value += card.value
        while numberOfAce > 0 :
            if self.value + 11 <= 21:
                self.value += 11
            else:
                self.value += 1
            numberOfAce -= 1
    def ClearCards(self):
        self.cards.clear()
        self.value = 0
        
#the PlayerHand class inherents from the Hand class
#Then adds the ability to keep track of thier coins
class PlayerHand(Hand):
    def __init__ (self,coins = 50):
        Hand.__init__(self)
        self.coins = coins   
    def addCoins(self,value):
        self.coins += value
    
    def removeCoins(self,value):
        self.coins -= value

'''      
The DealerHand class inherents from the Hand class
Then adds the ability to keep track of the value for only the 
first card in the Dealers hand. This is because
when the player first starts, only the first card
of the dealer is visable.
'''      
class DealerHand(Hand):
    def __init__ (self):
        Hand.__init__(self)
        self.halfValue = 0
        
    def setHalfValue(self,card):
        self.halfValue = card.value
    def getHalfValue(self):
        return self.halfValue
        
        
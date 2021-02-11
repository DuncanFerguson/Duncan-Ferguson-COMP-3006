import random


class Card:
    """ Card Class to keep track of the card details (suit/color, value, etc."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

##Display The Face Cards
    def __str__(self):
        """Displaying the cards face values"""
        displayval = str(self.value)  # shallow copy?
        if self.value == 1: displayval = "Ace"
        elif self.value == 11: displayval = "Jack"
        elif self.value == 12: displayval = "Queen"
        elif self.value == 13: displayval = "King"
        return displayval + " of " + self.suit


class Deck:
    """ Building a Deck out of the Cards"""
    def __init__(self):
        """Storying a Deck of Cards"""
        self.cards = []
        self.create_deck()

    def create_deck(self):
        """Making a normal 52 card deck. Ace counting as 1"""
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        """Shuffling the Deck three times. It is more of a wash pile shuffle than
        traditional"""
        random.shuffle(self.cards)

    def show_deck(self):
        """Used for testing reasons"""
        for card in self.cards:
            card.show()

    def deck_count(self):
        """Used for testing reasons"""
        print(len(self.cards))

    def dealcard(self):
        """Deal a card and pop it off of the deck"""
        single_card = self.cards.pop()
        return single_card


class Table:
    """Creating a class of Players"""
    players = []

    def __init__(self, player):
        """Storing Player Info"""
        self.players.append(player)

    def showtable(self):
        print(self.players)

    def return_table(self):
        return self.players

class Hand:
    def __init__(self, nam):
        self.name = nam  # Naming the players hand
        self.cards = []  # No Cards in the hand to start
        self.value = 0  # Hand Starts with a count of zero
        self.ace_count = 0  # Adding in count for aces

    def add_card(self, card):
        """Adding the value of the card. All face cards are 10. Ace's are either 1 or 11 depending on the count"""
        self.cards.append(card)  # Add a card to the hand
        if 1 < card.value < 11: self.value += card.value
        elif card.value == 13: self.value += 10
        elif card.value == 12: self.value += 10
        elif card.value == 11: self.value += 10
        elif card.value == 1:  # Dealing with the aces
            self.value += 11
            self.ace_count = 1
        if self.ace_count == 1 and self.value > 21:
            self.value -= 10
            self.ace_count = 0


def show_hand(player, name):
    """Showing the Players Hand"""
    print(name, "Cards: ")
    for card in player.cards:
        print(card)
    print("Total Count:", player.value, "\n")


def loophit(hittinghand, name, deck):
    """Looping through hits"""
    keephitting = True
    while keephitting:
        if hittinghand.value == 21:
            return hittinghand.value
        elif hittinghand.value > 21:
            print(name, "Busts\n")
            return 0
        elif hittinghand.value < 21:
            if name == "Dealer" and hittinghand.value < 17:  # Dealer Auto hits unless at 17
                hittinghand.add_card(deck.dealcard())
                print("Dealer Hits\n")
                show_hand(hittinghand, name)
                pass
            elif name == "Dealer" and hittinghand.value >= 17:
                print("Dealer Stays\n")
                return hittinghand.value
            else:
                h_n = input("Would you Like another Card (Y/N)?\n")
                if h_n.lower() == "y":
                    hittinghand.add_card(deck.dealcard())
                    show_hand(hittinghand, name)
                elif h_n.lower() == "n":
                    print(name, "Stays\n")
                    return hittinghand.value


def scoretable(game_dict):
    """This function scores the table and determines the winner"""
    #TODO Make sure the dealer wins if there is a tie
    print(game_dict)

    maxhand = list(game_dict.values())
    # players = list(game_dict.keys())
    winning_hand = max(maxhand)
    for player in game_dict:
        if game_dict[player] == winning_hand:
            if player == "Dealer":
                print(player," wins with ", winning_hand)
            else:
                print(player, " wins with ", winning_hand)


def dealgame():
    """Dealing the Game"""
    playgame = input("Would You Like To Play Black Jack (Y/N)?\n")
    if playgame.lower() == "y":
        deck = Deck()
        deck.shuffle()
    else:
        print("Good Bye")
        exit()

    seat = Table("Dealer")
    num_players = int(input("How Many Players? "))
    for seat in range(num_players):
        seat = Table(input("Enter Player Name: "))
    member_score_dict = {}

    #Dealing deck for both players
    for member in seat.return_table():
        member_hand = Hand(member)
        member_hand.add_card(deck.dealcard())
        member_hand.add_card(deck.dealcard())
        show_hand(member_hand, member)
        member_score_dict[member] = loophit(member_hand, member, deck)

    scoretable(member_score_dict)
    print("Game Over\n")
    # dealgame()


def main():
    """Starting the Game"""
    dealgame()


main()

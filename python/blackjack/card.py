from random import sample
from os import system

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __int__(self):
        if "H" in self.suit:
            return 0
        elif self.rank == "A":
            return 11
        elif self.rank in ["J", "Q", "K"]:
            return 10
        else:
            return int(self.rank)

    def __str__(self):
        if "H" in self.suit:
            return "--"
        return self.rank + self.suit


class Deck:
    def __init__(self, num_of_decks = 1):
        self._cards = []
        for d in range(num_of_decks):
            for s in ["♠", "♣", "♦", "♥"]:
                for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                    self._cards.append(Card(s,r))

    def shuffle(self):
        self._cards = sample(self._cards, len(self._cards))

    def pop(self):
        return self._cards.pop()


class Hand:
    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        s = ""
        for c in self._cards:
            s += f"{str(c)} "
        s += f"\nThe total is: {int(self)}"
        return s

    def __int__(self):
        total = 0
        aces = 0
        for c in self._cards:
            if int(c) == 11:
                aces += 1
            total += int(c)

        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    def draw(self, deck):
        self._cards.append(deck.pop())

    def hidden_draw(self, deck):
        c = deck.pop()
        c.suit += "H"
        self._cards.append(c)

    def reveal(self):
        for c in self._cards:
            c.suit = c.suit.strip("H")


class Game:
    def __init__(self):
        self.deck = ""
        self.dealers_hand = ""
        self.players_hand = ""
        self.player_blackjack = False
        self.dealer_blackjack = False
        self.insurance = False

    def start_game(self, new_deck, num_of_decks = 1):
        if new_deck:
            self.deck = Deck(num_of_decks)
            self.deck.shuffle()
        self.dealers_hand = Hand()
        self.players_hand = Hand()
        self.players_hand.draw(self.deck)
        self.players_hand.draw(self.deck)
        self.dealers_hand.hidden_draw(self.deck)
        self.dealers_hand.draw(self.deck)
        self.player_blackjack = False
        self.dealer_blackjack = False
        self.insurance = False

    def run_game(self):
        if not self.players_turn():
            self.dealers_turn()
        return input("(A)nother game or (Q)uit: ").upper() == "A"

    def print_game(self):
        system("clear")
        print("The Dealer's Hand:")
        print(f"{self.dealers_hand}\n\n")
        print("The Player's Hand:")
        print(f"{self.players_hand}\n\n")

    def players_turn(self):
        command = ""
        while command != "S" and int(self.players_hand) < 21:
            self.print_game()
            command = input("(H)it, (S)tay, or (Q)uit: ").upper()
            if command == "H":
                self.players_hand.draw(self.deck)
            elif command == "S":
                pass
            elif command == "Q":
                exit()
            else:
                print("Not a valid input")
                sleep(1)

        self.dealers_hand.reveal()
        self.print_game()
        return self.finish_players_turn()

    def finish_players_turn(self):
        if int(self.players_hand) > 21:
            print("Player Busts")
            self.dealer_win(False)
        elif self.player_blackjack and self.dealer_blackjack:
            self.tie()
        elif self.dealer_blackjack and not self.player_blackjack:
            self.dealer_win(True, self.insurance)
        elif self.player_blackjack and not self.dealer_blackjack:
            self.player_win(True)
        else:
            return False
        return True

    def dealers_turn(self):
        while int(self.dealers_hand) < 17:
            self.dealers_hand.draw(self.deck)
            print("The dealer will hit")
            input("Press enter to continue:")
            self.print_game()
        print("The dealer will stay")
        input("Press enter to continue:")
        self.finish_dealers_turn()

    def finish_dealers_turn(self):
        d, p = int(self.dealers_hand), int(self.players_hand)
        if d > 21:
            print("Dealer Busts")
            self.player_win(False)
        elif d == p:
            self.tie()
        elif d > p:
            self.dealer_win(False)
        elif d < p:
            self.player_win(False)

    def tie(self):
        print("Push")

    def player_win(self, blackjack):
        if blackjack: print("Blackjack!")
        print("Player Wins!")

    def dealer_win(self, blackjack, insurance = False):
        if blackjack: print("Blackjack!")
        print("Dealer Wins")

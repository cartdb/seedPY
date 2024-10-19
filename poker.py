from treys import Deck # 52-card deck
from treys import Card # 
from treys import Evaluator
import time
deck = Deck()
player1 = 100
player2 = 100
decksize = 52
while player1 > 0 and player2 > 0:
    evaluator = Evaluator()
    pot = 0
    player1 -= 10
    player2 -= 10
    pot += 20
    if decksize - 2 < 0:
        deck = Deck()
        decksize = 52
    player1_hand = deck.draw(2)
    decksize -= 2
    if decksize - 2 < 0:
        deck = Deck()
        decksize = 52
    player2_hand = deck.draw(2)
    decksize -= 2
    hands = [player1_hand, player2_hand]
    Card.print_pretty_cards(player1_hand)
    if decksize - 3 < 0:
        deck = Deck()
        decksize = 52
    board = deck.draw(3)
    decksize -= 3
    Card.print_pretty_cards(board)
    if decksize - 1 < 0:
        deck = Deck()
        decksize = 52
    board = board + deck.draw(1)
    decksize -= 1
    if decksize - 1 < 0:
        deck = Deck()
        decksize = 52
    board = board + deck.draw(1)
    decksize -= 1
    Card.print_pretty_cards(board)
    Card.print_pretty_cards(player2_hand)
    p1_score = evaluator.evaluate(board, player1_hand)
    p2_score = evaluator.evaluate(board, player2_hand)
    p1_class = evaluator.get_rank_class(p1_score)
    p2_class = evaluator.get_rank_class(p2_score)
    print("Player 1 hand rank = %d (%s)\n" % (p1_score, evaluator.class_to_string(p1_class)))
    print("Player 2 hand rank = %d (%s)\n" % (p2_score, evaluator.class_to_string(p2_class)))
    if p1_score < p2_score:
        player1 += pot
    elif p1_score > p2_score:
        player2 += pot
    elif p1_score == p2_score:
        player1 += pot / 2
        if int(player1) == player1:
            player1 = int(player1)
        player2 += pot / 2
        if int(player2) == player2:
            player2 = int(player2)
    print("Player 1: " + str(player1))
    print("Player 2: " + str(player2))
    time.sleep(1)
if player1 > player2:
    print("Player 1 wins!")
elif player2 > player1:
    print("Player 2 wins!")
else:
    print("Tie!")
import random


# from replit import clear
# from art import logo

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose,opponent has Blackjack"
    elif user_score == 0:
        return "win with a balckjack"
    elif user_score > 21:
        return "you went over. you lose"
    elif computer_score > 21:
        return "opponent went over. you win"
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"


def play_game():
    # print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards:{user_cards},current score:{user_score}")
        print(f"computer's first card:{computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"your final hand:{user_cards},final score:{user_score}")
    print(f"computer's final hand:{computer_cards},final score:{computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of balckjack?type 'y' or 'no':") == "y":
    # clear()
    play_game()

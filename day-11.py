import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and 10 in cards:
        if len(cards) == 2:
            return 0
    if 11 in cards:
        if score > 21:
            cards.remove(11)
            cards.append(1)

    return score

def compare(ur_score, cr_score):
    if ur_score == cr_score:
        print("That's a draw")
    elif cr_score == 0:
        print("You lose!. Opponent has BLACKJACK")
    elif ur_score == 0:
        print("You win with a BLACKJACK!")
    elif ur_score > 21:
        print("You went over. You lose")
    elif cr_score > 21:
        print("Computer went over. You win")
    elif ur_score > cr_score:
        print("You win")
    else:
        print("You lose")

def black_jack():
    ur_cards = []
    cr_cards = []

    for x in range(2):
        ur_cards.append(deal_card())
        cr_cards.append(deal_card())

    game_over = False
    while not game_over:
        ur_score = calculate_score(ur_cards)
        cr_score = calculate_score(cr_cards)
        print(f"Your cards: {ur_cards},current score: {ur_score}")
        print(f"Computer's 1st card: {cr_cards[0]}")

        if ur_score == 0 or cr_score == 0 or ur_score > 21:
            game_over = True
        else:
            draw_again = input("Would you like to draw another card? Yes or no?: ").lower()
            if draw_again == "yes":
                ur_cards.append(deal_card())
                calculate_score(ur_cards)
            else:
                game_over = True

    while cr_score != 0 and cr_score < 17:
        cr_cards.append(deal_card())
        cr_score = calculate_score(cr_cards)

    print(f"Your cards: {ur_cards},final score: {ur_score}")
    print(f"Computer's cards: {cr_cards}, final score: {cr_score}")
    compare(ur_score, cr_score)


    play_again = input("Do you wanna play again? Yes or no?: ").lower()
    if play_again == "yes":
        black_jack()
    else:
        game_over = True

black_jack()
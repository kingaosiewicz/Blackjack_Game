from art import logo
import random
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(cards):
    """ Zwraca pseudolosową kartę z listy """
    return random.choice(cards)

def calculate_score(cards):
    """
    Zwraca sumę kart, zamieniając asa (11) na 1 w razie potrzeby.
    """
    score = sum(cards)
    aces = cards.count(11)

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

def blackjack():
    """Główna funkcja gry w Blackjacka."""
    print(logo)

    # Rozdanie startowe
    player_cards = [deal_card(deck), deal_card(deck)]
    current_score = calculate_score(player_cards)
    computer_cards = [deal_card(deck), deal_card(deck)]
    computer_score = calculate_score(computer_cards)

    print(f"Your cards: {player_cards}. Current score: {current_score}")
    print(f"Dealer's first card: [{computer_cards[0]}]")

    # Sprawdzenie blackjacka po rozdaniu
    if computer_score == 21:
        print("Dealer has Blackjack. You lose!")
        return
    elif current_score == 21:
        print("Blackjack! You win!")
        return

    # --- TURA GRACZA ---
    while current_score < 21:
        choice = input("Type 'yes' to get another card, type 'no' to pass: ")

        if choice.lower() == 'yes':
            player_card = deal_card(deck)
            player_cards.append(player_card)
            current_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}. Current score: {current_score}")

        elif choice.lower() == 'no':
            break

        else:
            print("Invalid input.")

    # --- TURA KRUPIERA ---
    while computer_score < 17:
        new_card = deal_card(deck)
        computer_cards.append(new_card)
        computer_score = calculate_score(computer_cards)

    # --- WYNIKI KOŃCOWE ---
    print(f"Your final hand {player_cards}. Final score {current_score}")
    print(f"Dealer's final hand {computer_cards}. Final score {computer_score}")

    if current_score > 21:
        print("You went over. Dealer wins!")
    elif computer_score > 21:
        print("Dealer went over. You win!")
    elif current_score > computer_score:
        print("You win! Dealer loses.")
    elif computer_score > current_score:
        print("You lose! Dealer wins.")
    else:
        print("Draw!")
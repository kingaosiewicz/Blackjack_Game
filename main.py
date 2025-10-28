from functions import blackjack

# --- START GRY ---
if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ").lower() == 'yes':
        print(100*"\n")
        blackjack()
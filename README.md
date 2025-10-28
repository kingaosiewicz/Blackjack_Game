# Blackjack Game

### Description
This project is a console-based implementation of the Blackjack card game. The game allows a single player to play against the computer (dealer), following standard Blackjack rules. Players aim to get a hand value as close as possible to 21 without exceeding it, while the dealer follows a simple set of rules to draw cards. The program handles card dealing, score calculation, and game outcomes automatically.

### Features
- Randomly deals cards to both player and computer.
- Automatically calculates the score, including handling of Blackjack (Ace as 1 or 11).
- Allows the player to choose whether to draw additional cards or pass.
- Dealer draws cards according to standard rules (must draw until reaching at least 17).
- Determines the winner based on player and dealer scores, including Blackjack and bust scenarios.
- Continuous gameplay with option to start a new game after finishing one.

### How It Works
1. The player and the dealer are each dealt two cards at the start.
2. The player can choose to draw additional cards or pass.
3. If the player's hand exceeds 21, they bust and lose automatically.
4. The dealer draws cards until reaching a score of at least 17.
5. The program compares the final scores to determine the winner.
6. After the game ends, the player can choose to play again.

### Example

<pre>Your cards: [3, 3]. Current score: 6
Dealer's first card: [10]
Type 'yes' to get another card, type 'no' to pass: yes
Your cards: [3, 3, 10]. Current score: 16
Type 'yes' to get another card, type 'no' to pass: yes
Your cards: [3, 3, 10, 10]. Current score: 26
Your final hand [3, 3, 10, 10]. Final score 26
Dealer's final hand [10, 8]. Final score 18
You went over. Dealer wins! </pre>

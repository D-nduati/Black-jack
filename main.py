from random import choice

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]


def determine_winner(users_total, computer_total, computer_dealt_cards,
                     computer_first, computer_second):
    full_hand = [computer_first, computer_second] + computer_dealt_cards

    # Player busts
    if users_total > 21:
        return "Lose", full_hand

    # Player has blackjack
    if users_total == 21:
        return ("Draw" if computer_total == 21 else "Win"), full_hand

    # Computer has blackjack
    if computer_total == 21:
        return "Lose", full_hand

    # Computer draws until it stands (>=17) or busts
    while computer_total <= 16:
        print("Computer Total Cards is Less than 16... ")
        card = choice(cards)
        computer_dealt_cards.append(card)
        computer_total += card
        print(f"Computer dealt card is {card}. Computer Total Is: {computer_total}")

        if computer_total > 21:
            return "Win", [computer_first, computer_second] + computer_dealt_cards

    # Compare final totals
    if computer_total > 21:
        return "Win", [computer_first, computer_second] + computer_dealt_cards
    if users_total == computer_total:
        return "Draw", [computer_first, computer_second] + computer_dealt_cards
    if users_total > computer_total:
        return "Win", [computer_first, computer_second] + computer_dealt_cards
    return "Lose", [computer_first, computer_second] + computer_dealt_cards


def show_answer(result, full_hand):
    if result == "Win":
        print(f"You won! Computer Cards are: {full_hand}")
    elif result == "Lose":
        print(f"You lost! Computer Cards are: {full_hand}")
    else:
        print(f"It's a draw! Computer Cards are: {full_hand}")


def play_game() -> None:
    first_num = choice(cards)
    second_num = choice(cards)
    users_total = first_num + second_num

    computer_first = choice(cards)
    computer_second = choice(cards)
    computer_dealt_cards = []
    computer_total = computer_first + computer_second

    print(f"Your cards are: {[first_num, second_num]}  Total: {users_total}")
    print(f"Computer First Card: {computer_first}, _")

    # Single game loop
    while users_total <= 21:
        users_choice = input("Type 'Y' to stand or 'n' to hit: ").strip().lower()

        if users_choice == "y":
            result, full_hand = determine_winner(
                users_total, computer_total, computer_dealt_cards,
                computer_first, computer_second
            )
            show_answer(result, full_hand)
            return

        elif users_choice == "n":
            card = choice(cards)
            users_total += card
            print(f"Your Dealt Card: {card}. Total is: {users_total}")

            if users_total > 21:
                result, full_hand = determine_winner(
                    users_total, computer_total, computer_dealt_cards,
                    computer_first, computer_second
                )
                show_answer(result, full_hand)
                return
        else:
            print("Invalid choice. Please type 'Y' or 'n'.")


if __name__ == "__main__":
    while input("Do you want to Play Black Jack?\nType 'y' to Play or 'n' to Exit: ").strip().lower() == "y":
        play_game()
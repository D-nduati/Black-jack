from random import choice
cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]


first_num = choice(cards)
second_num = choice(cards)
users_total = first_num + second_num
computer_first = choice(cards)
computer_second = choice(cards)
computer_dealt_cards=[]

is_game_over = False


computer_total = computer_first + computer_second

formated_answer = f'Your cards are:{[first_num,second_num]}:Computer First Card:{computer_first,"_"}'



def determine_winner(users_total, computer_total):
    if users_total >=22:
        return "Lose"
    elif computer_total <=16:
        while computer_total <=16:
            print("Computer Total Cards is Less than 16... ")
            computer_dealt_card = choice(cards)
            computer_dealt_cards.append(computer_dealt_card)
            computer_total += computer_dealt_card
            print(f"Computer dealt card is {computer_dealt_card} Computer Total Is: {computer_total}")
            if computer_total >=22:
                return "Win"
            elif computer_total == users_total:
                return "Draw"
            elif computer_total>users_total:
                return "Lose"
            else:
                continue
    elif users_total == computer_total:
        return "Draw"
    elif users_total > computer_total:
        return "Win"
    else:
        return "Lose"
def show_answer(result):
    global is_game_over
    if result == 'Win':
        if computer_dealt_cards:
            computer_dealt_cards.append(computer_first)
            computer_dealt_cards.append(computer_second)
            print(f"You won!:Computer Cards are: {computer_dealt_cards}")
            is_game_over=True
        else:
            print(f"You won!:Computer Cards are: [{computer_first,computer_second}]")
            is_game_over = True
    elif result == 'Lose':
        if computer_dealt_cards:
            computer_dealt_cards.append(computer_first)
            computer_dealt_cards.append(computer_second)
            print(f"You Lost !:Computer cards are: {computer_dealt_cards}")
            is_game_over = True
        else:
            print(f"You lost!:Computer Cards are: [{computer_first,computer_second}]")
            is_game_over = True
    else:
        print("It's a draw!")
        is_game_over = True

while not is_game_over:
    print(formated_answer)
    users_choice= input('Type Y to stand or n to hit:')
    if users_choice == 'Y':
        result = determine_winner(users_total, computer_total)
        show_answer(result)
    else:
        users_3_choice = choice(cards)
        users_total += users_3_choice
        print(f"Your Dealt Card: {users_3_choice}: Total is: {users_total}")
        if users_total>=22:
            result = determine_winner(users_total, computer_total)
            show_answer(result)
            is_game_over= True
        while True:
            users_choice = input('Type Y to stand or n to hit:')
            if users_choice == 'Y':
                result = determine_winner(users_total, computer_total)
                show_answer(result)
                break
            elif users_choice == 'n':
                users_dealt_card = choice(cards)
                users_total += users_dealt_card
                print(f"Your Dealt Card: {users_dealt_card}: Total is: {users_total}")
                if users_total >=22:
                    result = determine_winner(users_total, computer_total)
                    show_answer(result)
                    break
            else:
                print('Invalid Choice')
while True:
    continue_game = input('Type "y" to Play or "n" to Exit:')
    if continue_game == 'y':
        is_game_over = False
    elif continue_game == 'n':
        break
    else:
        print("invalid choice")


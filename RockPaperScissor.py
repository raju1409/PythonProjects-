import random


def play():
    user = input('r for rock s for scissor p for paper : ')
    computer = random.choice(['r', 's', 'p'])
    if user not in ['r','s','p']:
        return 'invalid input'

    if user == computer:
        return 'TIE'
    if is_win(user, computer):
        return f'Your Choice :{user} and computer choice: {computer} "YOU WIN"'
    return f"Your Choice :{user} and computer choice: {computer} 'YOU LOSE!!!'"

    # r>s s>p p>r


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


print(play())

import random
from pyahtzee import combinations

dice_sides = {1:'⚀', 2:'⚁',3:'⚂',4:'⚃',5:'⚄',6:'⚅'}
initial_list_of_upper_combinations = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
initial_list_of_lower_combinations = ["One Pair", "Two Pairs", "Three of a Kind", "Four of a Kind", "Small Straight", "Large Straight", "Full House", "Chance", "Yahtzee"]
list_of_upper_combinations = initial_list_of_upper_combinations
list_of_lower_combinations = initial_list_of_lower_combinations
score = 0
rounds = 0

def round():
    rerolls_counter = 0
    result = []
    
    def roll_random_dice():
        return random.choices(range(1, 7), k=5)
    
    random_dice = roll_random_dice()
    random_dice.sort()
    
    def print_dice():
        for i, dice in enumerate(random_dice, start=1):
            print('[' + dice_sides[dice] + ' ' + str(dice) + ']', end=' ')
        print("\n")
    
    def reroll(*args):
        for dice in args:
            random_dice[dice-1] = random.randint(1, 6)
        random_dice.sort()
        nonlocal rerolls_counter    
        rerolls_counter += 1

    def reroll_choice():
        while True:
            user_input = input("Enter dice from 1 to 5 that you want to reroll separated by spaces: ")
            numeric_check = all(char.isdigit() or char.isspace() for char in user_input)
            if numeric_check:
                range_check = all(int(char) >= 1 and int(char) <= 5 for char in user_input.split())
                if range_check:
                    break
        dice_to_reroll = user_input.split()
        result_list = []
        for dice in dice_to_reroll:
            result_list.append(int(dice))
        return result_list
    
    while rerolls_counter < 2:
        print_dice()

        while True:
            user_input = input("Do you want to reroll dice?(y/n): ")
            if user_input == 'y':
                reroll(*reroll_choice())
                break
            elif user_input == 'n':
                rerolls_counter = 2
                result = random_dice
                break
    result = random_dice

    score = combinations.check_results(result)

    if combinations.results_list[-1] == "Yahtzee" and "Yahtzee" not in list_of_lower_combinations:
        print("Yahtzee bonus!")
        score += 100
    
    return score

def play():
    global score
    score += round()
    global rounds
    rounds += 1

    print("Your current score: " + str(score))
    print("\n")
    for combination in combinations.results_list:
        if combination in list_of_upper_combinations:
            list_of_upper_combinations.remove(combination)
        elif combination in list_of_lower_combinations:
                list_of_lower_combinations.remove(combination)
    
    print("Upper combinations left: ")
    for combination in list_of_upper_combinations:
        print(combination, end="; ")
    print("\n")    
    print("Lower combinations left: ")
    for combination in list_of_lower_combinations:
        print(combination, end="; ")
    print("\n")    
    print("Next round: " + str(rounds + 1))

def game():
    global rounds
    global score
    global list_of_upper_combinations
    global list_of_lower_combinations
    if rounds == 0:
        while True:
            ask = input("Do you want to play a game: ")
            if ask == "y":
                while rounds < 13:
                    play()
                print("Your final score: " + str(score))
                print("Thank you for the game!")
                score = 0
                rounds = 0
                list_of_upper_combinations = initial_list_of_upper_combinations
                list_of_lower_combinations = initial_list_of_lower_combinations
                combinations.results_list = []
            elif ask == "n":
                break
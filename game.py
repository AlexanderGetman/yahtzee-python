import random
import combinations

dice_sides = {1:'⚀', 2:'⚁',3:'⚂',4:'⚃',5:'⚄',6:'⚅'}

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
            user_input = input("Enter dices from 1 to 6 that you want to reroll separated by spaces: ")
            numeric_check = all(char.isdigit() or char.isspace() for char in user_input)
            if numeric_check:
                range_check = all(int(char) >= 1 and int(char) <= 5 for char in user_input.split())
                if range_check:
                    break
        dices_to_reroll = user_input.split()
        result_list = []
        for dice in dices_to_reroll:
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
                result = random_dice
                return result
    result = random_dice
    return result

print(combinations.check_results(round()))
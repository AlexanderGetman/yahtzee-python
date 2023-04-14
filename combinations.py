from collections import Counter

def check_results(result):
    print("Dices: ")
    print(result)
    upper_result = check_results_upper_section(result)
    lower_result = check_results_lower_section(result)

    print("Results are: ")
    print(upper_result)
    print(lower_result)

def check_results_upper_section(result):
    combinations = []
    
    if result.count(1) >= 1:
        combinations.append("Ones. Score: " + str(result.count(1) * 1))
    if result.count(2) >= 1:
        combinations.append("Twos. Score: " + str(result.count(2) * 2))
    if result.count(3) >= 1:
        combinations.append("Threes. Score: " + str(result.count(3) * 3))
    if result.count(4) >= 1:
        combinations.append("Fours. Score: " + str(result.count(4) * 4))
    if result.count(5) >= 1:
        combinations.append("Fives. Score: " + str(result.count(5) * 5))
    if result.count(6) >= 1:
        combinations.append("Sixes. Score: " + str(result.count(6) * 6))

    return combinations

def check_results_lower_section(result):
    combinations = []

    if one_pair(result):
        combinations.append("One Pair. Score: " + str(one_pair(result)))
    if two_pairs(result):
        combinations.append("Two Pairs. Score: " + str(two_pairs(result)))
    if three_of_a_kind(result):
        combinations.append("Three of a Kind. Score: " + str(three_of_a_kind(result)))
    if four_of_a_kind(result):
        combinations.append("Four of a Kind. Score: " + str(four_of_a_kind(result)))
    if small_straight(result):
        combinations.append("Small Straight. Score: " + str(small_straight(result)))
    if large_straight(result):
        combinations.append("Large Straight. Score: " + str(large_straight(result)))
    if full_house(result):
        combinations.append("Full House. Score: " + str(full_house(result)))
    if chance(result):
        combinations.append("Chance. Score: " + str(chance(result)))
    if yahtzee(result):
        combinations.append("Yahtzee! Score: " + str(yahtzee(result)))

    return combinations

def one_pair(my_list):
    duplicates = []
    max_number = 0
    for num in my_list:
        if my_list.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    if duplicates:        
        for num in duplicates:
            if num > max_number:
                max_number = num
    return max_number * 2

def two_pairs(my_list):
    duplicates = []
    for num in my_list:
        if my_list.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
    if len(duplicates) == 2:
        return sum(duplicates) * 2

def three_of_a_kind(my_list):
    result = None
    for num in my_list:
        if my_list.count(num) > 2 and num != result:
            result = num
    if result:
        return result * 3

def four_of_a_kind(my_list):
    result = None
    for num in my_list:
        if my_list.count(num) > 3 and num != result:
            result = num
    if result:
        return result * 4

def small_straight(result):
    small_straight = [1, 2, 3, 4, 5]
    result.sort()
    if result == small_straight:
        return 15

def large_straight(result):
    small_straight = [2, 3, 4, 5, 6]
    result.sort()
    if result == small_straight:
        return 20

def full_house(my_list):
    pair = None
    three_of_a_kind = None
    for num in my_list:
        if my_list.count(num) == 3:
            three_of_a_kind = num

    for num in my_list:
        if my_list.count(num) == 2 and num != three_of_a_kind:
            pair = num

    if pair and three_of_a_kind:
        return (pair * 2) + (three_of_a_kind * 3)

def chance(my_list):
    return sum(my_list)

def yahtzee(my_list):
    if all(num == my_list[0] for num in my_list):
        return 50
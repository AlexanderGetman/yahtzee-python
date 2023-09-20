from collections import Counter

results_list = []
score_list = []

def check_results(result):
    print("Dice: ")
    print(result)
    upper_result, upper_scores = check_results_upper_section(result)
    lower_result, lower_scores = check_results_lower_section(result)

    for result in results_list:
        if result in upper_result:
            position = upper_result.index(result)
            upper_scores.pop(position)
            upper_result.remove(result)
        elif result in lower_result:
            position = lower_result.index(result)
            lower_scores.pop(position)
            lower_result.remove(result)

    print("Upper results are: ")
    for i, res in enumerate(upper_result, start=1):
        print(str(i) + ". " + res + ", Score: " + str(upper_scores[i - 1]))

    print("Lower results are: ")
    for i, res in enumerate(lower_result, start=1):
        print(str(i) + ". " + res + ", Score: " + str(lower_scores[i - 1]))
    
    def select_results():
        score = None

        if len(upper_result) == 0 and len(lower_result) == 0:
            score = 0
            return score

        while True:            
            select_section = input("Select section (u / l): ")
            if select_section == "u":
                select_combination = input("Select combination: ")
                if select_combination.isnumeric():
                    if int(select_combination) <= len(upper_result) and int(select_combination) != 0:
                        select_combination = int(select_combination) - 1
                        results_list.append(upper_result[select_combination])
                        score = upper_scores[select_combination]
                        break
            elif select_section == "l":                
                select_combination = input("Select combination: ")
                if select_combination.isnumeric():
                    if int(select_combination) <= len(lower_result) and int(select_combination) != 0:
                        select_combination = int(select_combination) - 1
                        results_list.append(lower_result[select_combination])
                        score = lower_scores[select_combination]
                        break
        return score
        
    score = select_results()
    score_list.append(score)
    return score

def check_results_upper_section(result):
    combinations = []
    scores = []
    
    if result.count(1) >= 1:
        combinations.append("Ones")
        scores.append(result.count(1) * 1)
    if result.count(2) >= 1:
        combinations.append("Twos")
        scores.append(result.count(2) * 2)
    if result.count(3) >= 1:
        combinations.append("Threes")
        scores.append(result.count(3) * 3)
    if result.count(4) >= 1:
        combinations.append("Fours")
        scores.append(result.count(4) * 4)
    if result.count(5) >= 1:
        combinations.append("Fives")
        scores.append(result.count(5) * 5)
    if result.count(6) >= 1:
        combinations.append("Sixes")
        scores.append(result.count(6) * 6)

    return combinations, scores

def check_results_lower_section(result):
    combinations = []
    scores = []

    if one_pair(result):
        combinations.append("One Pair")
        scores.append(one_pair(result))
    if two_pairs(result):
        combinations.append("Two Pairs")
        scores.append(two_pairs(result))
    if three_of_a_kind(result):
        combinations.append("Three of a Kind")
        scores.append(three_of_a_kind(result))
    if four_of_a_kind(result):
        combinations.append("Four of a Kind")
        scores.append(four_of_a_kind(result))
    if small_straight(result):
        combinations.append("Small Straight")
        scores.append(small_straight(result))
    if large_straight(result):
        combinations.append("Large Straight")
        scores.append(large_straight(result))
    if full_house(result):
        combinations.append("Full House")
        scores.append(full_house(result))
    if chance(result):
        combinations.append("Chance")
        scores.append(chance(result))
    if yahtzee(result):
        combinations.append("Yahtzee")
        scores.append(yahtzee(result))

    return combinations, scores

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

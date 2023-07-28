import random

def deal_card():
    """ Get a Random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(arr):
    """Calculate total in the given array"""
    total = sum(arr)
    # for i in range(len(arr)):
    #     total += arr[i]
    
    return total

def generate_opening_card(list):
    list.append(deal_card())
    list.append(deal_card())
    return list

def pick_card(list):
    list.append(deal_card())
    return list

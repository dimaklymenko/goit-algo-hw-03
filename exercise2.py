import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers_set = set()
    while len(lottery_numbers_set) != quantity:
        lottery_numbers_set.add(random.randint(min, max))
    return sorted(list(lottery_numbers_set))
    # return sorted(random.sample(range(min, max), quantity))    


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
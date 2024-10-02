import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min <= 0 or max > 1000:
            empty_list = []
            print("min має бути >=1 та max має бути <=1000")
            return empty_list
        elif min > max:
            empty_list = []
            print("min має бути менше за max")
            return empty_list
        elif max-min < quantity:
            empty_list = []
            print("quantity має бути <= max-min")         
            return empty_list
        else:
            lottery_numbers_set = set()
            while len(lottery_numbers_set) != quantity:
                lottery_numbers_set.add(random.randint(min, max))
            return sorted((lottery_numbers_set))    # return sorted(random.sample(range(min, max), quantity))       
    except Exception:
        pass
lottery_numbers = get_numbers_ticket(900, 1020, 30)
print("Ваші лотерейні числа:", lottery_numbers)
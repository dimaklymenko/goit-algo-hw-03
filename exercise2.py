import random

def get_numbers_ticket(min, max, quantity):
    try:
        if min <= 0 or max > 1000:
            empty_list = []
            return print(f"min має бути >=1 та max має бути <=1000, {empty_list}")      # return empty_list щоб повернуло порожній список
        elif min > max:
            empty_list = []
            return print(f"min має бути менше за max {empty_list}")         # return empty_list щоб повернуло порожній список
        elif len(range(min, max)) < quantity-1:
            empty_list = []
            return print(f"quantity-1 має бути <= len(range(min, max)), {empty_list}")          # return empty_list щоб повернуло порожній список
        else:
            lottery_numbers_set = set()
            while len(lottery_numbers_set) != quantity:
                lottery_numbers_set.add(random.randint(min, max))
            return sorted(list(lottery_numbers_set))    # return sorted(random.sample(range(min, max), quantity))       
    except Exception:
        pass
lottery_numbers = get_numbers_ticket(10, 15, 9)
print("Ваші лотерейні числа:", lottery_numbers)
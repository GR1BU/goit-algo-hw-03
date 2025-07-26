import random

def get_numbers_ticket(min, max, quantity):
    if not 1 <= min <=max <=1000 or quantity > (max - min + 1):
        return []
    

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

print(get_numbers_ticket(1, 1000, 15))
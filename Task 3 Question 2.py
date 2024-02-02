def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

original_list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = [num for num in original_list if is_prime(num)]

print("Prime Numbers:", prime_numbers)

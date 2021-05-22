def is_armstrong_number(number):
    digits, power = str(number), len(str(number))
    return sum([pow(int(i), power) for i in digits]) == number

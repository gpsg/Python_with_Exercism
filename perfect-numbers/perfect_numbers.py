def classify(number):
    if number < 1:
        raise ValueError(f"{number} is not a positive integer")
    aliquot = sum([i for i in range(1, number) if number % i == 0])
    if aliquot != number:
        return "abundant" if aliquot > number else "deficient"
    return "perfect"

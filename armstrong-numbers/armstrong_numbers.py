def is_armstrong_number(number):
    digits = list(map(lambda x: int(x), str(number)))
    factor = len(digits)
    return sum(pow(x, factor) for x in digits) == number

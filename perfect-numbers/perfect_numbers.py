def classify(number):
    if number < 1:
        raise ValueError("Should be a natural number greater than 0")
    aliquot = aliquot_sum(number)
    if aliquot == number:
        return "perfect"
    if aliquot > number:
        return "abundant"
    if aliquot < number:
        return "deficient"

def aliquot_sum(number):
    return sum(factors(number))

def factors(n):
    return [i for i in range(1, n//2 + 1) if n % i == 0]
    
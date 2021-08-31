def leap_year(year):
    mult4 = year % 4 == 0
    mult100 = year % 100 == 0
    mult400 = year % 400 == 0
    return mult4 and (not(mult100) or mult400)

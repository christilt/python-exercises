YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12

def score(dice, category):
    if category == ONES:
        return sum(filter(lambda x: x == 1, dice))
    if category == TWOS:
        return sum(filter(lambda x: x == 2, dice))
    if category == THREES:
        return sum(filter(lambda x: x == 3, dice))
    if category == FOURS:
        return sum(filter(lambda x: x == 4, dice))
    if category == FIVES:
        return sum(filter(lambda x: x == 5, dice))
    if category == SIXES:
        return sum(filter(lambda x: x == 6, dice))
    if category == FULL_HOUSE:
        three_of_kind_nos = set(filter(lambda x: __of_kind_exact(dice, x, 3), 
                                         __nos))
        two_of_kind_nos = set(filter(lambda x: __of_kind_exact(dice, x, 2), 
                                       __nos))
        full_house = any(three_of_kind_nos.difference(two_of_kind_nos))
        return sum(dice) if full_house else 0
    if category == FOUR_OF_A_KIND:
        four_of_kind_nos = filter(lambda x: __of_kind(dice, x, 4), __nos)
        four_of_kind_no = next(four_of_kind_nos, 0)
        return four_of_kind_no * 4
    if category == LITTLE_STRAIGHT:
        return 30 if all(x in dice for x in [1,2,3,4,5]) else 0
    if category == BIG_STRAIGHT:
        return 30 if all(x in dice for x in [2,3,4,5,6]) else 0
    if category == CHOICE:
        return sum(dice)
    if category == YACHT:
        five_of_kind_nos = filter(lambda x: __of_kind(dice, x, 5), __nos)
        return 50 if any(five_of_kind_nos) else 0

        

def __of_kind(dice, kind, count):
    """ True if there are at least count elements in dice matching kind """
    return len(list(filter(lambda x: x == kind, dice))) >= count

def __of_kind_exact(dice, kind, count):
    """ True if there are exactly count elements in dice matching kind """
    return len(list(filter(lambda x: x == kind, dice))) == count

__nos = [1, 2, 3, 4, 5, 6]


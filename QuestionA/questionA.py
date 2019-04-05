def isOverlapping(line1, line2):
    if not isinstance(line1, tuple) or not isinstance(line2, tuple):
        raise Exception('Lines must be tuples')

    if len(line1) is not 2 or len(line2) is not 2:
        raise Exception('Lines must contain 2 positions')

    if not tupleContainsIntegers(line1) or not tupleContainsIntegers(line2):
        raise Exception('Positions must be integers')

    line1 = sorted(line1)
    line2 = sorted(line2)

    if(line1[1] >= line2[0] and line2[1] >= line1[0]):
        return True
    return False


def tupleContainsIntegers(tuple):
    for item in tuple:
        if not isinstance(item, int):
            return False
    return True

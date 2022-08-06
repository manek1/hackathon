def get_bit_and(num1, num2):
    """
    :param num1:
    :param num2:
    :return: result of bitwise and as integer
    """
    if isInteger(num1) and isInteger(num2):
        return bitwiseAnd(num1, num2)
    else:
        return False

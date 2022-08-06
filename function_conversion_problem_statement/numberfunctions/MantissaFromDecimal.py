def get_mantissa(num1):
    """
    :param num1:
    :return: Returns the mantissa from the given decimal/numeric string/integer num1
    """
    num1 = toDouble(num1)
    num1 = toString(num1)
    mantissa = num1.split('.')
    return toInteger(mantissa)
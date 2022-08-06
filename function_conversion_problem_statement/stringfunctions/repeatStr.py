def repeat_str(str1, repeat=0):
    """
    :param str1:
    :param repeat:
    :return: repeats a string the specified number of times
    """
    while repeat > 0:
        str1 = concat(str1, str1)
    return str1

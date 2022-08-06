def get_field(str1, delimiter, occurrence, step = 1):
    """
    :param str1:
    :param delimiter:
    :param occurrence:
    :param step:
    :return: returns one or more substrings that are located between specified delimiters in a string
    """
    str_arr = str1.split(delimiter)
    op_str = ''
    if len(str_arr) < occurrence:
        return ''
    elif step == 1:
        op_str = str_arr[occurrence-1]
        return op_str
    else:
        while step > 0 and occurrence < len(str_arr):
            if op_str == '':
                op_str = str_arr[occurrence-1]
            else:
                op_str = concat(op_str, delimiter , str_arr[occurrence-1])
            occurrence += 1
            step -= 1
        return op_str
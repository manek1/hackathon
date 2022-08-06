def compare_str(str1, str2, justification='R'):
    """
    :param str1:
    :param str2:
    :param justification:
    :return: 1 or 0
    """
    if justification == 'R':
        if length(str1) > length(str2):
            return 1
        elif length(str1) < length(str2):
            return -1
        else:
            return 0
    elif justification == 'L':
        if length(str1) < length(str2):
            return 1
        elif length(str1) > length(str2):
            return -1
        else:
            return 0
    else:
        return None

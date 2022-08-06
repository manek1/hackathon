def get_minutes_from_time(input_time):
    """
    :param input_time:
    :return: Minutes as integer
    """
    minute = toString(input_time)
    return toInteger(substring(minute, 4, 2))
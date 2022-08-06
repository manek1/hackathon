def get_timet_from_timestamp(input_time_stamp):
    """
    :param input_time_stamp:
    :return: returns time in the form of unix timestamp
    """
    unix_time = div(sub(ticks(input_time_stamp), ticks('1970-01-01')), 10000000)
    return unix_time

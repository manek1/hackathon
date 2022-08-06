def get_date_from_days_since2(num_of_days, start_date):
    """
    :param num_of_days:
    :param start_date:
    :return: Returns date after adding the days
    """
    new_date = addDays(toDate(start_date), num_of_days)
    return new_date

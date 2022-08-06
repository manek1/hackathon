def check_is_null(col):
    """
    :param col:
    :return: boolean, True if value is null else False
    Didn't implemented the same way as in datastage where the null check runs column as not aware about ADF to iterate
    Column row by row
    """
    if isNull(col):
        return False
    else:
        return True

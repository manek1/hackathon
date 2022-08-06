def get_Null_To_Value(col_val, fill_val):
    """
    :param col_val:
    :param fill_val:
    :return: col_val if col_val is not null else fill_val
    :note: Didn't implemented the same way as in datastage where the null check runs column as not aware about ADF to iterate
    Column row by row
    """
    if isNull(col_val):
        return fill_val
    else:
        return col_val

def replace_sub_str(str1, sub_str, replace_with, occurrence=None, replace_index=None):
    """
    :param str1:
    :param sub_str:
    :param replace_with:
    :param occurrence:
    :param replace_index:
    :return: string after replacing sub_str with replace_with frm str1
    """
    temp_str = str1[:]
    occurrences_counter = 0
    sub_str_len = length(sub_str)
    start_indexes = []

    while temp_str != '':
        occurrence_flag = locate(sub_str, temp_str)
        if occurrence_flag == 0:
            temp_str = ''
        else:
            occurrences_counter += 1
            start_indexes.append(occurrence_flag)
            start_indexes = occurrence_flag + sub_str_len
            temp_str = temp_str[start_indexes:]

    if occurrence < occurrences_counter and not replace_index:
        index_last = start_indexes[occurrence - 1] + sub_str_len
        sub_str_replace = str1[:index_last]
        sub_str_unchanged = str1[index_last:]
        op_str = replace(sub_str_replace, sub_str, replace_with)
        op_str = concat(op_str, sub_str_unchanged)
        return op_str
    elif occurrence < occurrences_counter and replace_index:
        index_first = replace_index[0]
        index_last = replace_index[1]
        sub_str_replace = str1[index_first:index_last]
        op_str = replace(sub_str_replace, sub_str, replace_with)
        op_str = concat(str1[:index_first], op_str, str1[index_last:])
        return op_str
    else:
        op_str = replace(str1, sub_str, replace_with)
        return op_str

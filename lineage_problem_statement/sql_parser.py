import sqlparse


def parse_sql(sql_stmt, file_flag='F'):
    sql_stmt_list = list()

    if file_flag.upper() == 'F':
        try:
            with open(sql_stmt, 'r') as sql_fd:
                pass

        except FileNotFoundError:
            print("Unable to find the sql file")

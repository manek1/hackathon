import sys
import getopt
import get_tables
import get_col


def match_parahs(str1):
    cnt_o = 0
    cnt_c = 0
    for char in str1:
        if char.strip() == '(':
            cnt_o += 1
        if char.strip() == ')':
            cnt_c += 1
    if cnt_o == cnt_c and cnt_o != 0 and cnt_c != 0:
        return True
    else:
        return False


def get_alias(col_name):
    # Note use sortedDict package if your not using python version 3.5+
    alias_dtl = {}
    if col_name.lower().rfind(' as ') == -1:
        as_s = col_name.split(' ')
        if len(as_s) == 2:
            alias_dtl[as_s[0]] = as_s[1]
        elif match_parahs(col_name):
            spc = col_name.rfind(" ")
            brac = col_name.rfind(')')
            print(spc)
            print(brac)
            if spc > brac:
                alias_dtl[col_name[:spc]] = col_name[spc + 1:]
            else:
                alias_dtl[col_name] = ''
        else:
            alias_dtl[col_name] = ''
    elif col_name.lower().rfind(' as ') > -1:
        a_psn = col_name.lower().rfind(' as ')
        alias_dtl[col_name[:a_psn]] = col_name[a_psn + 4:]
    return alias_dtl


def get_c_name(col_name):
    actual_col_name = ''
    if col_name.lower().rfind(' as ') == -1:
        as_s = col_name.split(' ')
        if len(as_s) == 2:
            actual_col_name = as_s[1]
    elif col_name.lower().rfind(' as ') > -1:
        a_psn = col_name.lower().rfind(' as ')
        actual_col_name = col_name[a_psn + 4:]
    else:
        actual_col_name = col_name
    return actual_col_name


def remove_dbs(tbl_names):
    op_tbl_names = {}
    for als, tbl_name in tbl_names.items():
        op_tbl_nm = tbl_name.split('.')
        op_tbl_names[als] = op_tbl_nm
    return op_tbl_names


def map_col_tbl(col_names, tbl_names):
    tbl_col_map = {}
    n_tbl_names = remove_dbs(tbl_names)
    for col_name in col_names:
        tbl = col_name[-1]
        if tbl in n_tbl_names.keys():
            tbl_col_map[col_name] = n_tbl_names[tbl]
    return tbl_col_map


def unfold_col(col):
    col_names_derived = []
    col_names = []
    alias_c = {}
    if col:
        for col_name in col:
            col_name = col_name.strip()
            # if match_parahs(col_name):
            alias_c = get_alias(col_name)
            if alias_c:
                col_names
                for col_a_name, col_alias in alias_c.items():
                    col_names.append(str(col_a_name))
                    if col_alias != '':
                        col_names_derived.append(str(col_alias) + ' derived from ' + str(col_a_name))
                    else:
                        col_names_derived.append(str(col_a_name))

    print(col_names_derived, col_names)


if __name__ == '__main__':
    argv = sys.argv[1:]
    sql_file_path, sql_query = None, None
    file_flag = 'F'
    no_arc = 1
    num_args = len(argv)
    if num_args == 0:
        print("Missing mandatory parameter sql file or query")
        exit(1)
    else:
        try:
            options, arguments = (getopt.getopt(argv, 'f:q:', ["sql_file_path=", "sql_query="]))
        except OSError:
            print("Error in getting script arguments")
            exit(1)
        for opt, arg in options:
            print(opt, arg)
            if opt in ['-f', '--sql_file_path']:
                sql_file_path = arg
            elif opt in ['-q', '--sql_query']:
                sql_query = arg
        if sql_file_path is None and sql_query is None:
            print("Missing mandatory parameter sql file or query")
            exit(1)
        if sql_query is not None:
            sql_qry = get_col.parse_sql(sql_query, file_flag='Q')
            col_names = get_col.extract_column_names(sql_qry)
            tbl_names = get_tables.extract_tables(str(sql_qry))
            cl_tables = map_col_tbl(col_names, tbl_names)

            if cl_tables:
                for col_name, tbl_name in cl_tables.items():
                    print(col_name, " =>", tbl_name)
            else:
                print("No mapping found in given sql")
        else:
            sql_qrys = get_col.parse_sql(sql_file_path)
            for sql_qry in sql_qrys:
                col_names = get_col.extract_column_names(sql_qry)
                tbl_names = get_tables.extract_tables(str(sql_qry))
                cl_tables = map_col_tbl(col_names, tbl_names)

                if cl_tables:
                    for col_name, tbl_name in cl_tables.items():
                        print(col_name, " =>", tbl_name)
                else:
                    print("No mapping found in given sql")



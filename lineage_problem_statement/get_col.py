import sqlparse
from sqlparse.tokens import Keyword, CTE, DML
from sqlparse.sql import Identifier, IdentifierList, Parenthesis


def parse_sql(sql_stmt, file_flag='F'):
    sql_stmt_list = []
    if file_flag.upper() == 'F':
        try:
            with open(sql_stmt, 'r') as sql_fd:
                sql_qrys = sql_fd.read()
                sql_qry = sqlparse.parse(sql_qrys)
                return sql_qry
        except FileNotFoundError:
            print("Unable to find the sql file")
    elif file_flag.upper() == 'Q':
        sql_qry = sqlparse.parse(sql_stmt)
        return sql_qry


def _identifiers(tok):
    if isinstance(tok, IdentifierList):
        for t in tok.get_identifiers():
            # print(type(t))
            if isinstance(t, Identifier):
                yield str(t)
    elif isinstance(tok, Identifier):
        type(tok)
        yield str(tok)


def extract_column_names(parsed):
    idx, tok = parsed.token_next_by(t=DML)
    tok_val = tok and tok.value.lower()

    if tok_val in ("insert", "update", "delete"):
        idx, tok = parsed.token_next_by(idx, (Keyword, "returning"))
    elif not tok_val == "select":
        return ()
    # The next token should be either a column name, or a list of column names
    idx, tok = parsed.token_next(idx, skip_ws=True, skip_cm=True)
    # print(tok)
    return list(t for t in _identifiers(tok))

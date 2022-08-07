import sqlparse
from sqlparse.tokens import Keyword, CTE, DML
from sqlparse.sql import Identifier, IdentifierList, Parenthesis


def is_subselect(parsed):
    if not parsed.is_group:
        return False
    for item in parsed.tokens:
        if item.ttype is DML and item.value.upper() == 'SELECT':
            return True
    return False


def extract_from_part(parsed):
    from_seen = False
    for item in parsed.tokens:
        if from_seen:
            if is_subselect(item):
                yield from extract_from_part(item)
            elif item.ttype is Keyword:
                return
            else:
                yield item
        elif item.ttype is Keyword and item.value.upper() == 'FROM':
            from_seen = True


def extract_table_identifiers(token_stream):
    # print(type(token_stream))
    for item in token_stream:
        # print(type(item))
        if isinstance(item, IdentifierList):
            for identifier in item.get_identifiers():
                yield str(identifier)  # identifier.get_name()
        elif isinstance(item, Identifier):
            yield str(item)  # item.get_name()
        elif item.ttype is Keyword:
            yield str(item.value)


def extract_tables(sql):
    stream = extract_from_part(sqlparse.parse(sql)[0])
    return list(extract_table_identifiers(stream))

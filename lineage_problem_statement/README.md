# RUN Commands

#Through File
    python map_tables.py -f test_sqs.txt
                    or
    python map_tables.py --sql_file_path test_sqs.txt

#Passing sql
    python map_tables.py -q "select a.c_name, b.n_id from a;"
                     or
    python map_tables.py --sql_query test_sqs.txt
# RUN Commands

#Through File
    python map_tables.py -f test_sqs.txt

#Passing sql
    python map_tables.py -s "select a.c_name, b.n_id from a;"
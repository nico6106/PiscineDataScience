import psycopg2
from time import time
from typing import Any


def time_decorator(func):
    """compute performance in s"""
    def inner(*args: Any, **kwds: Any):
        """inner function of perf function"""
        """eliminate args"""
        init = time()
        result = func(*args)
        end = time()
        total = end - init
        print(f"==>Function {func.__name__} took : {total}s")
        return result
    return inner


def drop_table(cur, name):
    try:
        sql = f"""DROP TABLE {name};"""
        print(f'cmd=\'{sql}\'')
        cur.execute(sql)
        print(f'table {name} deleted')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return


def is_table(cur, name) -> bool:
    """check if name is already a table in DB"""
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
        """)
    data_tables = cur.fetchall()
    for elem in data_tables:
        if elem.count(name) != 0:
            print(f"{name} already exists")
            return True
    return False

def delete_duplicates(cur, name):
    """delete duplicates"""
    sql = f"""
DELETE FROM {name} t1
USING {name} t2
WHERE t1.event_time < t2.event_time 
OR (t1.event_time = t2.event_time
AND t1.event_type = t2.event_type
AND t1.product_id = t2.product_id
AND t1.price = t2.price
AND t1.user_id = t2.user_id
AND t1.user_session = t2.user_session);
"""

# event_type, product_id, price, user_id = user_id, user_session, COUNT (*) AS count
# FROM {name} = name}
# GROUP BY event_type, product_id, price, user_id, user_session
# HAVING COUNT (*) > 1;
# """
    print(sql)
    cur.execute(sql)
    res = cur.fetchone()[0]
    print(res)
    return


def select_duplicates(cur, name):
    """select duplicates"""
    sql = f"""SELECT event_type, product_id, price, user_id, user_session, COUNT (*) AS count
FROM {name}
GROUP BY event_type, product_id, price, user_id, user_session
HAVING COUNT (*) > 1;
"""

# event_time

# 	sql = f"""SELECT DISTINCT *
# FROM {name} t1
# WHERE EXISTS (
#     SELECT *
#     FROM {name} t2
#     WHERE t1.event_type = t2.event_type
#     AND   t1.product_id = t2.product_id
#     AND   t1.price = t2.price
#     AND   t1.user_id = t2.user_id
#     AND   t1.user_session = t2.user_session )
# """
    
#     SELECT * 
# FROM {name} A
# USING {name} B
# WHERE A.event_type = B.event_type
# AND A.product_id = B.product_id
# AND A.price = B.price
# AND A.user_id = B.user_id
# AND A.user_session = B.user_session
# """
    print(sql)
    cur.execute(sql)
    result = cur.fetchall()
    return result

    # event_time
    # event_type
    # product_id
    # price
    # user_id
    # user_session


def print_x_rows(data, nb_rows):
    i = 0
    len_data = len(data)
    while i < nb_rows and i < len_data:
        print(f"{i} = {data[i]}")
        i = i + 1

@time_decorator
def main():
    """Main function of the program"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="piscineds",
            user="nlesage",
            password="mysecretpassword")
        print('Connected to DB')
        conn.autocommit = True
        cur = conn.cursor()
        # drop_table(cur, 'customers')
        if is_table(cur, 'customers') is True:
            duplicates = select_duplicates(cur, 'customers')
            print(f"duplicates:")
            print(f"len={len(duplicates)}")
            print(f"type{type(duplicates)}")
            print_x_rows(duplicates, 10)
            
            delete_duplicates(cur, 'customers')
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn = None
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    return


if __name__ == "__main__":
    main()

# oct	4102283
# nov	4635837
# dec	3533286
# jan	4264752
# feb	4156682
	
# tot	20692840

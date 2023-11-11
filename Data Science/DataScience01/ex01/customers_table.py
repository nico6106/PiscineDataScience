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


def create_table(cur, name: str):
    """create a table"""
    sql = f"""CREATE TABLE {name} (
    event_time timestamp NOT NULL,
    event_type VARCHAR(255),
    product_id int,
    price float,
    user_id bigint,
    user_session uuid
);"""
    cur.execute(sql)
    print('table created')


def get_all_data_table_names(cur):
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';
        """)
    all_tables = cur.fetchall()
    data_tables = []
    for table in all_tables:
        if 'data_202' in table[0]:
            data_tables.append(table[0])
    return data_tables


def join_data(cur):
    tab_names = get_all_data_table_names(cur)
    print(tab_names)
    name = 'data_2022_oct'
    for name in tab_names:
        sql = f"""INSERT INTO customers (event_time,event_type,product_id,price,user_id,user_session)
SELECT * FROM {name};"""
        cur.execute(sql)
    return


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
        if is_table(cur, 'customers') is False:
            create_table(cur, 'customers')
            join_data(cur)
        
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

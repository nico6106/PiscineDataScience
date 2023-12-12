import psycopg2
import os
# import pandas as pd
from time import time
from typing import Any
# from sqlalchemy import create_engine, types


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


@time_decorator
def verif_file(folder, file) -> str:
    """verif file name + if exists and return path if correct"""
    path = folder + file
    if not type(path) is str:
        raise AssertionError('Incorrect path')
    if not path.lower().endswith('csv'):
        raise AssertionError('Incorrect format')
    if not os.path.exists(path):
        raise AssertionError(f'{file} does not exist')
    return path


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


@time_decorator
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


@time_decorator
def insert_data(cur, path, name):
    """insert data to table"""
    # data = pd.read_csv(path)
    sql = f"""COPY {name}(event_time,event_type,product_id,
    price,user_id, user_session)
    FROM '{path}'
    DELIMITER ','
    CSV HEADER;"""
    cur.execute(sql)
#     data_type = {
#         "event_time": types.DateTime(),
#         "event_type": types.String(),
#         "product_id": types.Integer(),
#         "price": types.Float(),
#         "user_id": types.BigInteger(),
#         "user_session": types.Uuid(as_uuid=True),
#     }
#     engine = create_engine("postgresql://nlesage:mysecretpassword\
# @localhost/piscineds")
#     data.to_sql(name, engine, index=False, if_exists='replace',
#                 dtype=data_type)
    print('data imported')


def drop_table(cur, name):
    try:
        sql = f"""DROP TABLE {name};"""
        print(f'cmd=\'{sql}\'')
        cur.execute(sql)
        print(f'table {name} deleted')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return


def main(folder, file):
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

        # drop_table(cur, 'data_2022_oct')

        if is_table(cur, 'data_2022_oct') is False:
            # verif path
            path = verif_file(folder, file)
            # create table
            create_table(cur, 'data_2022_oct')
            # feed table with csv file
            folder_docker = '/tmp/'
            path = folder_docker + file
            insert_data(cur, path, 'data_2022_oct')

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
    folder = '/mnt/nfs/homes/nlesage/sgoinfre/\
nlesage/DataScience/subject/customer/'
    file = 'data_2022_oct.csv'
    main(folder, file)

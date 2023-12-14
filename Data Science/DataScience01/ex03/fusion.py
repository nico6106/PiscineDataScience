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


def left_join_tables(cur, name):
    """function that left join the datas"""
#     sql = """ALTER TABLE customers 
# ADD COLUMN category_id bigint,
# ADD COLUMN category_code text,
# ADD COLUMN brand text"""
#     cur.execute(sql)
    
	# creer table cust bis
    sql = """CREATE TABLE customers_bis (
    event_time timestamp NOT NULL,
    event_type VARCHAR(255),
    product_id int,
    price float,
    user_id bigint,
    user_session uuid,
    category_id bigint,
    category_code text,
    brand text);"""
    cur.execute(sql)
    
	#creer table item_bis pour supprimer les doublons
    sql = """CREATE TABLE item_bis(
product_id int,
category_id bigint,
category_code text,
brand text
)"""
    cur.execute(sql)
    
	# inserer que les valeurs uniques "completes" dans la table item_bis
    sql = """INSERT INTO item_bis (product_id, category_id, category_code, brand)
SELECT
    "product_id",
    MAX("category_id") AS "category_id",
    MAX("category_code") AS "category_code",
    MAX("brand") AS "brand"
FROM
    item
GROUP BY
    "product_id";"""
    cur.execute(sql)
    
    # delete temporary table if exists
    sql = """INSERT INTO customers_bis
SELECT customers.event_time, customers.event_type, customers.product_id, customers.price, customers.user_id, customers.user_session, 
    item_bis.category_id, item_bis.category_code, item_bis.brand
FROM customers
LEFT JOIN item_bis ON customers.product_id = item_bis.product_id;"""
    cur.execute(sql)
    
	# supprimer table customers initiale
    sql = """DROP TABLE customers"""
    cur.execute(sql)
    
	# supprimer table item_bis
    sql = """DROP TABLE item_bis"""
    cur.execute(sql)
    
	# renommer cutomers_bis en customers
    sql = """ALTER TABLE customers_bis RENAME TO customers;"""
    cur.execute(sql)
    print("left join executed")
    print(sql)
            
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
        if is_table(cur, 'customers') is True:
            left_join_tables(cur, 'customers')
        
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


# ALTER TABLE customers 
# ADD COLUMN category_id bigint,
# ADD COLUMN category_code text,
# ADD COLUMN brand text

# SELECT customers.*, item.*
# FROM customers
# LEFT JOIN item ON customers.product_id = item.product_id;




# INSERT INTO item_bis SELECT * FROM item


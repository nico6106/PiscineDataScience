import psycopg2
from time import time
from typing import Any
import matplotlib.pyplot as plt


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


def import_data(cur):
    """function that imports data needed"""
    cur.execute("""SELECT DISTINCT event_type FROM customers""")
    event_types = [elem[0] for elem in cur.fetchall()]

    # get nbs for all types
    event_nb = []
    for elem in event_types:
        sql = f"""SELECT COUNT (*) FROM customers WHERE event_type = '{elem}';"""
        cur.execute(sql)
        nb = cur.fetchall()[0][0]
        event_nb.append(nb)

    # print(f"event types: {event_types} = {event_nb}")
    # print(f"sum = {sum(event_nb)}")
    events = [event_types, event_nb]
    return events


def draw(data):
    plt.pie(data[1], labels=data[0], autopct='%1.1f%%')
    # plt.legend(data[0])
    plt.show()
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
            data = import_data(cur)
            print(f"data = {data}")
            # data = [['cart', 'purchase', 'remove_from_cart', 'view'], [5108887, 1286045, 2688869, 9441450]]
            draw(data)
            

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
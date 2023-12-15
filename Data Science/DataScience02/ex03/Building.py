import psycopg2
from time import time
from typing import Any
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd



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


def nb_order_frequency(cur):
    cur.execute("""select count(user_session), user_id
from customers_clean
where event_type = 'purchase'
group by user_id
""")
    datas = cur.fetchall()
    data = pd.DataFrame(datas)
    data = data[0]
    
    tab_y = [0, 0, 0, 0, 0]
    tab_x = ['[0-10[', '[10-20[', '[20-30[', '[30-40[', '40+']
    for elem in data:
        if elem <= 9: tab_y[0] = tab_y[0] + 1
        elif elem <= 19: tab_y[1] = tab_y[1] + 1
        elif elem <= 29: tab_y[2] = tab_y[2] + 1
        elif elem <= 39: tab_y[3] = tab_y[3] + 1
        else: tab_y[4] = tab_y[4] + 1

    # print(data_avg.describe())
    plt.hist(data, bins=5, edgecolor='k')
    # plt.ylabel('customers')
    plt.xlabel('frequency')
    plt.xticks(range(0, 39, 10))
    plt.ylim(0, 60000)

    plt.show()

    # plt.bar(tab_x, tab_y)
    # plt.xlabel('frequency')
    # plt.ylabel('customers')
    # plt.show()
    return


def spent_by_cust(cur):
    cur.execute("""select sum(price), user_id
from customers_clean
where event_type = 'purchase'
group by user_id;
""")
    datas = cur.fetchall()
    data = pd.DataFrame(datas)
    data = data[0]
    
    tab_y = [0, 0, 0, 0, 0]
    tab_x = ['[0-20[', '[20-50[', '[50-100[', '[100-200[', '200+']
    for elem in data:
        if elem < 20: tab_y[0] = tab_y[0] + 1
        elif elem < 50: tab_y[1] = tab_y[1] + 1
        elif elem < 100: tab_y[2] = tab_y[2] + 1
        elif elem < 200: tab_y[3] = tab_y[3] + 1
        else: tab_y[4] = tab_y[4] + 1

    # print(data_avg.describe())

    plt.bar(tab_x, tab_y)
    plt.xlabel('monetary value in A')
    plt.ylabel('customers')
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
        if is_table(cur, 'customers') is True:
            nb_order_frequency(cur)
            spent_by_cust(cur)

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
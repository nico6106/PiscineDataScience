import psycopg2
from time import time
from typing import Any
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from collections import defaultdict
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


def graph_nb_cust(cur):
    """function that imports data needed"""
    cur.execute("""SELECT event_time, price, user_id FROM customers WHERE event_type = 'purchase'""")
    datas = cur.fetchall()

    custs = pd.DataFrame(datas)
    custs = custs.rename(columns={0: 'event_time'})
    custs = custs.rename(columns={1: 'price'})
    custs = custs.rename(columns={2: 'user_id'})

    custs['event_time']  = custs['event_time'].dt.date
    info = custs.groupby(['event_time', 'user_id']).count()
    nb_clients = info.groupby('event_time').size().reset_index(name='nb_clients')
    
    plt.plot(nb_clients['event_time'], nb_clients['nb_clients'])
    plt.ylabel('Number of customers')
        
    formatter = mdates.DateFormatter('%b')
    plt.gca().xaxis.set_major_formatter(formatter)
    
    plt.show()
    
    # nb_clients = info.groupby('event_time').size().reset_index(name='nb_clients')
    
    # plt.plot(nb_clients['event_time'], nb_clients['nb_clients'])
    # plt.ylabel('Number of customers')
        
    # formatter = mdates.DateFormatter('%b')
    # plt.gca().xaxis.set_major_formatter(formatter)
    
    # plt.show()
    
    # print(f"{nb_clients}")
    

    # days = defaultdict(int)
	# # iterate on all datas and identify nb cust per day
    # for elem in datas:
    #     days[elem[0].date()] += 1
    
    # tab_days = []
    # tab_nb = []
    # for day, nb in days.items():
    #     tab_days.append(day)
    #     tab_nb.append(nb)
    
    # # for jour, nombre_clients in days.items():
    # #     print(f"Jour {jour}: {nombre_clients} clients")
    # #     break

    # plt.plot(tab_nb)
    # plt.show()
    return 


def graph_total_sales(cur):
    """function that imports data needed"""
    cur.execute("""SELECT event_time, price, user_id FROM customers WHERE event_type = 'purchase'""")
    datas = cur.fetchall()

    custs = pd.DataFrame(datas)
    custs = custs.rename(columns={0: 'event_time'})
    custs = custs.rename(columns={1: 'price'})
    custs = custs.rename(columns={2: 'user_id'})

    custs['event_time']  = custs['event_time'].dt.date
    
    info = custs.groupby('event_time').sum()
    print(info)
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
            # graph_nb_cust(cur)
            graph_total_sales(cur)

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
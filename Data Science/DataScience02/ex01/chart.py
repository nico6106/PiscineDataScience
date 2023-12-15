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
    dic_month = {10: "Oct", 11: "Nov", 12: "Dec", 1: "Jan", 2: "Feb"}
    cur.execute("""SELECT event_time, price FROM customers_clean WHERE event_type = 'purchase'""")
    datas = cur.fetchall()

    columns = ['event_time', 'price']
    custs = pd.DataFrame(datas, columns=columns)

    custs['event_time']  = custs['event_time'].dt.date
    info = custs.groupby('event_time').sum()

    # print(f"nb rows={len(custs)}")
    sum_per_month = info.groupby([lambda x: x.year, lambda x: x.month])['price'].sum()

    # print(sum_per_month)

    tab_month = []
    tab_sum = []
    for (year, month), elem in sum_per_month.items():
        tab_month.append(dic_month[month])
        tab_sum.append(elem)
    print(f"month={tab_month}, sum={tab_sum}")
    plt.bar(tab_month, tab_sum)
    plt.xlabel('month')
    plt.ylabel('total in sales in millions of A')
    plt.show()
    
    return


def average_spent(cur):
    """function that show average spent/customers"""
    dic_month = {10: "Oct", 11: "Nov", 12: "Dec", 1: "Jan", 2: "Feb"}
    cur.execute("""SELECT date(event_time) AS purchase_date,
	count(DISTINCT user_id) AS nb_clients,
	SUM(price) AS total_price,
	SUM(price) / count(DISTINCT user_id) as avg
FROM customers_clean
WHERE event_type = 'purchase'
GROUP BY purchase_date;

""")
    datas = cur.fetchall()
    # print(datas)
    tab_dates = []
    tab_avg = []
    for elem in datas:
        tab_dates.append(elem[0])
        tab_avg.append(elem[3])
        # print(elem)
        # print(f"date={elem[0]}, avg={elem[3]}")
        # break

    plt.plot(tab_avg)
    plt.ylabel('Number of customers')
        
    # formatter = mdates.DateFormatter('%b')
    # plt.gca().xaxis.set_major_formatter(formatter)
    plt.show()

    # columns = ['purchase_date', 'nb_clients', 'total_price', 'avg']
    # custs = pd.DataFrame(datas, columns=columns)
    
    # print(custs)

    # custs['event_time']  = custs['event_time'].dt.date
    
    # print(custs)
    
    # info_sum = custs.groupby(['event_time', 'user_id']).sum()
    # info_count = custs.groupby(['event_time', 'user_id']).count()
    # nb_clients = info_sum.groupby('event_time').size().reset_index(name='nb_clients')
    # nb_sum = info_count.groupby('event_time').sum().reset_index()
    # print(info_count)
    # print(info_sum)
    # print(nb_clients)
    # print(nb_sum)
    # print(nb_clients['nb_clients'])
    # print(nb_clients[1])
    # print(nb_sum['price'])
    
    
    # average = []
    # days = []
    
    # for i in range(len(nb_clients['nb_clients'])):
    #     average.append(nb_sum['price'][i] / nb_clients['nb_clients'][i])
    #     print(f"elem={nb_sum['price'][i]}")
    # print(average)
    # print(f"starting")
    # i = 0
    # for elem in nb_clients.items():
    #     print(f"elem={elem}")
    #     i = i + 1
    #     if (i >= 5):
    #         break 
    # for i in range(len(nb_clients)):
    #     print(f"i={i}, nb_sum[i]={nb_sum[i]} / nb_clients[i]={nb_clients[i]}")
    #     average.append(nb_sum[i] / nb_clients[i])
    #     if i == 5:
    #         break 
    
    # info = custs.groupby('event_time').sum()

    # # print(f"nb rows={len(custs)}")
    # sum_per_month = info.groupby([lambda x: x.year, lambda x: x.month])['price'].sum()

    # # print(sum_per_month)

    # tab_month = []
    # tab_sum = []
    # for (year, month), elem in sum_per_month.items():
    #     tab_month.append(dic_month[month])
    #     tab_sum.append(elem)
    # print(f"month={tab_month}, sum={tab_sum}")
    # plt.bar(tab_month, tab_sum)
    # plt.xlabel('month')
    # plt.ylabel('total in sales in millions of A')
    # plt.show()
    

    # info = custs.groupby(['event_time', 'user_id']).count()
    # nb_clients = info.groupby('event_time').size().reset_index(name='nb_clients')
    
    # plt.plot(nb_clients['event_time'], nb_clients['nb_clients'])
    # plt.ylabel('Number of customers')
        
    # formatter = mdates.DateFormatter('%b')
    # plt.gca().xaxis.set_major_formatter(formatter)

    
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
            # graph_total_sales(cur)
            average_spent(cur)

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
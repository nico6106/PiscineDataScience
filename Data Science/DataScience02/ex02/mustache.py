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


def extract_print_data(cur):
    """function that show average spent/customers"""
    cur.execute("""select price
from customers_clean
where event_type = 'purchase' ;
""")
    datas = cur.fetchall()
    data = pd.DataFrame(datas)
    
    quartiles = data[0].quantile([0.25, 0.5, 0.75])
    print()
    print(f"count {data[0].count()}")
    print(f"mean {data[0].mean()}")
    print(f"std	{data[0].std()}")
    print(f"min	{data[0].min()}")
    print(f"25%	{quartiles[0.25]}")
    print(f"50%	{quartiles[0.50]}")
    print(f"75%	{quartiles[0.75]}")
    print(f"max	{data[0].max()}")
    return data[0]


def show_boxplot_prices(data):
    plt.boxplot(data, vert=False)
    plt.xlabel('price')
    plt.show()
    
    plt.boxplot(data, vert=False)
    plt.xlabel('price')
    plt.xlim(0, 13)
    plt.show()
    return


def show_avg_boxplt(cur):
    cur.execute("""select avg(subquery.total_sum), user_id from (
	select sum(price) as total_sum, user_id, user_session
	from customers_clean
	where event_type = 'purchase'
	group by user_id, user_session
) as subquery
group by user_id
""")
    datas = cur.fetchall()
    data = pd.DataFrame(datas)
    data_avg = data[0]

    # print(data_avg.describe())

    plt.boxplot(data_avg, vert=False)
    plt.xlabel('price')
    plt.xlim(0, 70)
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
            data = extract_print_data(cur)
            # show_boxplot_prices(data)
            show_avg_boxplt(cur)

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
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load


def format_x(data):
    """format x axis"""
    if (data >= 1000):
        str = f"{int(data / 1000)}k"
    else:
        str = f"{data}"
    return str


def show_graph(data_life: pd.DataFrame, data_income: pd.DataFrame):
    """function that plot data"""
    life_1900 = data_life['1900'].values
    income_1900 = data_income['1900'].values
    plt.scatter(income_1900, life_1900)
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.xscale('log')
    plt.xticks([300, 1000, 10000])
    formatter = ticker.FuncFormatter(lambda x, pos: f'{format_x(x)}')
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.show()
    return


def main():
    """Main function or the program"""
    try:
        data_life = load("../life_expectancy_years.csv")
        if data_life is None:
            return
        data_income = load("../income_per_person_gdppercap\
ita_ppp_inflation_adjusted.csv")
        if not (data_life is None or data_income is None):
            show_graph(data_life, data_income)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()

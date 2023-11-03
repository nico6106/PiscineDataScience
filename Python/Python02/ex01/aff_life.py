import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def show_graph(data: pd.DataFrame):
    plt.plot(data["France"])
    plt.show()
    return


def main():
    """Main function or the program"""
    try:
        data = load("../life_expectancy_years.csv")
        show_graph(data)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()
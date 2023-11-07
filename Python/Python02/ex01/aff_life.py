import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def show_graph(data: pd.DataFrame):
    """Function that load file and show data on a graph"""
    new_data = data[data["country"] == "France"]
    years = new_data.columns[1:].astype(int)  # pour retirer "country"
    data_france = new_data.values[:, 1:].flatten()
    plt.plot(years, data_france)
    plt.title('France Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.show()
    return


def main():
    """Main function or the program"""
    try:
        data = load("../life_expectancy_years.csv")
        if data is not None:
            show_graph(data)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()

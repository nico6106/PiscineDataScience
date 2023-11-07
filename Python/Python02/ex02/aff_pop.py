import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
from load_csv import load


def treat_data(data: pd.DataFrame):
    """amend data to convert it to float"""
    new_data = [(x.replace('M', '')) for x in data]
    new_data = [float(x) * 1000000 for x in new_data]
    return new_data


def show_graph(data: pd.DataFrame):
    """function that plot data"""
    new_data = data.loc[(data["country"] == "France")
                        | (data["country"] == "Belgium")]
    years = new_data.columns[1:].astype(int)  # pour retirer "country"
    data_belgium = new_data.values[0][1:].flatten()
    data_france = new_data.values[1][1:].flatten()
    data_belgium = treat_data(data_belgium)
    data_france = treat_data(data_france)
    plt.plot(years, data_france, label='France')
    plt.plot(years, data_belgium, label='Belgium')
    plt.legend(loc='lower right')
    plt.xlim(right=2050)
    plt.title('Population Projections')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.yticks([20000000, 40000000, 60000000])
    plt.xticks(range(1800, 2051, 40))
    formatter = ticker.FuncFormatter(lambda x, pos: f'{int(x/1000000)}M')
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.show()
    return


def main():
    """Main function or the program"""
    try:
        data = load("../population_total.csv")
        if data is not None:
            show_graph(data)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()

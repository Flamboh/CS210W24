'''
CS 210 Lab 6 - functions
Oliver Boorstein
'''

import matplotlib.pyplot as plt

def read_data(file_name: str) -> list:
    with open(file_name, "r") as file:
        result = [line.strip().split(",") for line in file]
    return result


def list_to_dict(a_list: list) -> dict:
    keys = [pair[0] for pair in a_list]
    values = [pair[1] for pair in a_list]
    # return { int(item[0][:4]): float(item[1]) for item in a_list }
    return { int(date[:4]):float(rain) for (date, rain) in zip(keys, values) }


def dict_to_list(a_dict: dict) -> list:
    return [[key, a_dict[key]] for key in a_dict]


def mean_rainfall(values: list) -> float:
        acc = 0
        for id, rain in values:
            acc += rain
        
        return acc / len(values)

    


if __name__ == "__main__":
    data = dict_to_list(list_to_dict(read_data("labs\lab6\\november_rain.csv")))
    year = [pair[0] for pair in data]
    rain = [pair[1] for pair in data]

    plt.plot(year, rain)
    plt.axhline(y=mean_rainfall(data), color = 'r', linestyle=":")    
    plt.show()

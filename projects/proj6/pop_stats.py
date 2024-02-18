'''
CIS 210 proj 6
Author: Oliver Boorstein
Credits: N/A
calculate some statistics from population.json
'''

import json
import statistics as stat


def read_data(file_name: str, keys: list) -> list:

    fin = open(file_name)

    data = json.load(fin)

    stats_arr = []

    for key in keys:
        current_list = []
        for index in range(len(data)):
            current_list.append(data[index][key])
        stats_arr.append(current_list)
    fin.close()

    return stats_arr

def stats(an_array: list) -> dict:
    '''
    return the stats of an array
    '''
    stats_dict = {
        'min': min(an_array), 
        'max': max(an_array), 
        'range': (max(an_array) - min(an_array)),
        'mean': round(stat.mean(an_array), 2), 
        'mode': stat.mode(an_array),
        'var': round(stat.variance(an_array), 2), 
        'stdev': round(stat.stdev(an_array), 2)
    }

    return stats_dict


def filter_arr(an_arr: list, low_lim=0) -> list:
    return [x for x in an_arr if x > low_lim]

def dict_to_list(a_dict: dict) -> list:
    return [[key, a_dict[key]] for key in a_dict]


def print_stats(file_name: str) -> None:

    data_arr = read_data(file_name, ['pop2023', 'growth', 'density'])


    stats_labels = [item[0] for item in dict_to_list(stats(data_arr[0]))]
    stats_labels[-1] = "st.dev."
    stats_labels[-2] = "variance"
    pop_stats = [item[1] for item in dict_to_list(stats(filter_arr(data_arr[0], 10000)))]
    growth_stats = [item[1] for item in dict_to_list(stats(data_arr[1]))]
    density_stats = [item[1] for item in dict_to_list(stats(data_arr[2]))]
    print(" " * 12, end='')
    for _ in range(len(stats_labels)):
        print("+" + '-' * 13, end='')
    print('+')
    print(" " * 12, end='|')
    for item in stats_labels:
        print(str(item).ljust(13), end='|')

    print()
    print(" " * 12, end='')
    for _ in range(len(stats_labels)):
        print("+" + '-' * 13, end='')
    print("+")

    print("population".ljust(12), end="|")
    for item in pop_stats:
        print(str(round(item, 2)).ljust(13), end='|')

    print()
    print(" " * 12, end='')
    for _ in range(len(stats_labels)):
        print("+" + '-' * 13, end='')
    print("+")

    print("growth".ljust(12), end="|")
    for item in growth_stats:
        print(str(round(item, 2)).ljust(13), end='|')

    print()
    print(" " * 12, end='')
    for _ in range(len(stats_labels)):
        print("+" + '-' * 13, end='')
    print("+")

    print("density".ljust(12), end="|")
    for item in density_stats:
        print(str(round(item, 2)).ljust(13), end='|')

    print()
    print(" " * 12, end='')
    for _ in range(len(stats_labels)):
        print("+" + '-' * 13, end='')
    print("+")

if __name__ == "__main__":
    # print(read_data("projects\proj6\population.json", ["pop2023", "growth"]))
    # print(filter_arr([0, -3, 5, 100, 3, -100]))
    print_stats("population.json")
    pass

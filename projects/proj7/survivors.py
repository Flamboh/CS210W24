from titanic import *
import matplotlib.pyplot as plt
import numpy as np




def titanic_bars_count(data: dict, bars: list):
    bases = sorted(list(set(bars)))

    pairs_list = list(zip(data[('Survived', int)], bars))

    segments_dict = {key: {} for key in bases}




    for key in segments_dict.keys():
        key_individuals = [int(pair[0]) for pair in pairs_list if pair[1] == key]
        key_survivors = np.count_nonzero(key_individuals)
        segments_dict[key] = {
            'Survived': key_survivors,
            'Died': len(key_individuals) - key_survivors,
        }


    print(segments_dict)

    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(len(bases))
    for key, i in zip(segments_dict.keys(), range(len(segments_dict.keys()))):
        bottom = np.zeros(len(bases))
        for boolean, segment in segments_dict[key].items():
            p = ax.bar(key, segment, width, label=boolean if i == 0 else '', bottom=bottom, color='r' if boolean == 'Died' else 'g')
            bottom += segment
    
    plt.ylabel('Count')

    ax.set_title(f"Count of survivors by gender")
    ax.legend(loc="upper right")

    plt.show()


def titanic_bars_percent(data: dict, bars: list):
    bases = sorted(list(set(bars)))

    pairs_list = list(zip(data[('Survived', int)], bars))

    segments_dict = {key: {} for key in bases}




    for key in segments_dict.keys():
        key_individuals = [int(pair[0]) for pair in pairs_list if pair[1] == key]
        key_survivors = np.count_nonzero(key_individuals)
        segments_dict[key] = {
            'Survived': 100 * key_survivors / len(key_individuals),
            'Died': 100 * (len(key_individuals) - key_survivors) / len(key_individuals),
        }


    print(segments_dict)

    width = 0.5

    fig, ax = plt.subplots()
    bottom = np.zeros(len(bases))
    for key, i in zip(segments_dict.keys(), range(len(segments_dict.keys()))):
        bottom = np.zeros(len(bases))
        for boolean, segment in segments_dict[key].items():
            p = ax.bar(key, segment, width, label=boolean if i == 0 else '', bottom=bottom, color='r' if boolean == 'Died' else 'g')
            bottom += segment
    
    plt.ylabel('Percentage')

    ax.set_title(f"% of survivors by gender")
    ax.legend(loc="upper right")

    plt.show()


if __name__ == "__main__":
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                'Fare': float, 'Embarked': str, 'FamilySize': int,
                'age_group': str}
    data = load_data('titanic_clean.csv', titanic_types)

    titanic_bars_count(data, data[('Sex', str)])

    titanic_bars_percent(data, data[('Sex', str)])
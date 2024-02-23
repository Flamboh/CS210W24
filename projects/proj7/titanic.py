# import titanic
import csv
import statistics as stat
import matplotlib.pyplot as plt
# Write your functions here


def load_data(filename: str, types: dict) -> dict:
    with open(filename, 'r') as fin:
        reader = csv.reader(fin)
        data = {}


        data = {key: [] for key in zip(types, types.values())}

        next(reader)
        
        for row in reader:
            for key, val in zip(data.keys(), row):
                    data[key].append(val)
    
    return data


def summarize(data: dict) -> None:
    for key in data.keys():
        print(f"Statistics for {key[0]}:")
        if key[1] == float or key[1] == int:
            num_list = [float(val) for val in data[key]]
            summary_dict = {
                'min': round(min(num_list), 1), 
                'max': round(max(num_list), 1),
                'mean': round(stat.mean(num_list), 1),
                'stdev': round(stat.stdev(num_list), 1),
                'mode': round(stat.mode(num_list), 1)
            }
            for k in summary_dict:
                print(f"{k.rjust(7)}: {str(summary_dict[k]).rjust(6)}")
        else:
            # unique values
            print(f"Number of unique values: {len(set(data[key]))}")
            # most common
            print(f"      Most common value: {stat.mode(data[key])}")
            
def pearson_corr(x: list, y: list) -> float:
    if len(x) != len(y):
        raise ValueError('The list parameters must have the same number of elements.')

    try:

        x_num_list = [float(val) for val in x]
        y_num_list = [float(val) for val in y]

    except ValueError as ve:
        raise ValueError('pearson_corr only works with int or float lists.')
    return round((stat.covariance(x_num_list, y_num_list)/(stat.stdev(x_num_list) * stat.stdev(y_num_list))), 2)  
    

def survivor_vis(data: dict, col_1: tuple, col_2: tuple) -> plt.Figure:
    survived = [float(val) for val in data[('Survived', int)]]
    data_col_1 = [float(val) for val in data[col_1]]
    data_col_2 = [float(val) for val in data[col_2]]
    
    figure = plt.figure(figsize= (8, 4))
    

    survived_x = []
    survived_y = []

    died_x = []
    died_y = []
    for m, x, y in zip(survived, data_col_1, data_col_2):
        if m:
            survived_x.append(x)
            survived_y.append(y)
        else:
            died_x.append(x)
            died_y.append(y)

    plt.scatter(survived_x, survived_y, color='g', marker='o', label='Survived')
    plt.scatter(died_x, died_y, color='r', marker='x', label='Died')
    
    plt.title('Survival of Titanic Passengers')
    plt.xlabel(col_1[0])
    plt.ylabel(col_2[0])
    plt.legend()
    plt.savefig(f'scatter_{col_1[0]}_{col_2[0]}.png')
    plt.show(block=False)



# ------ You shouldn't have to modify main --------
def main():
    """Main program driver for Project 3."""

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('titanic_clean.csv', titanic_types)
    

    # 3.2 Print informative summaries
    print("\nPart 3.2")
    summarize(data)

    print("\nPart 3.3")
    # 3.3 Compute correlations between age and survival

    corr_age_survived = pearson_corr(data[('Age', float)],
                                     data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_survived:3.2f}')

    # 3.3 Correlation between fare and survival
    corr_fare_survived = pearson_corr(data[('Fare', float)],
                                      data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_survived:3.2f}')

    # 3.3 Correlation between family size and survival
    corr_fare_survived = pearson_corr(data[('FamilySize', int)],
                                      data[('Survived', int)])
    print(f'Correlation between family size and survival is'
          f' {corr_fare_survived:3.2f}')

    # # 3.4 Visualize results
    fig = survivor_vis(data, ('Age', float), ('Fare', float))
    fig = survivor_vis(data, ('Age', float), ('Pclass', int))
    fig = survivor_vis(data, ('Age', float), ('Parch', int))


if __name__ == "__main__":
    main()

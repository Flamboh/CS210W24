# import pandas as pd

# def read_csv_file(file_name, types):
#     with open(file_name, "r") as file:
#         titanic = pd.read_csv(file)

#         new_column_names = dict(zip(titanic.columns, types.items()))
#         print(new_column_names)

#         filtered_titanic = titanic[list(types)]
#         # filtered_titanic.rename(new_column_names, errors='raise')
#         print("heloooooo", filtered_titanic.columns)
        
#         data_dict = {key: list(titanic[key]) for key in filtered_titanic.columns}

#         return data_dict

# if __name__ == "__main__":
#     titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
#                      'Sex': str,'Age': float, 'SibSp': int, 'Parch': int,
#                      'Fare': float, 'Embarked': str, 'FamilySize': int,
#                      'age_group': str}
#     data = read_csv_file('titanic_clean.csv', titanic_types)
#     for key, val in data.items():
#         print(key, val[:4])

    

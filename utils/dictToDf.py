import pandas as pd

def convert(dictionary):
    keys = []
    items = []
    for item in dictionary.items():
        keys.append(item[0])
        items.append(item[1])
    # Make the dataframe, sort it by column header (date), and return it
    return pd.DataFrame(data = [items], columns=keys, index = [0]).sort_index(axis=1)
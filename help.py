import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def p(text):
    print('-' * 200)
    print(text)
    print('-' * 200)

def get_mgmt_chain(data, id_col='fid', employee='name', manager='manager', ceo_fid=181):

    data.loc[data[id_col] == ceo_fid, manager] = np.nan
    data[[employee, manager]] = data[[employee, manager]].replace(r' \(On Leave\)', '', regex=True)
    manager_dict = data.loc[:, [employee, manager]].set_index(employee).to_dict()[manager]

    chain = []
    for employee in data[employee]:
        manager = manager_dict[employee]
        individual_chain = [manager]
        while not pd.isnull(manager):
            manager = manager_dict[manager]
            if not pd.isnull(manager):
                individual_chain.append(manager)
        chain.append(individual_chain)
    data['chain'] = chain
    data = data.astype({'chain': 'str'})

    return data

def label_graph(data, x, y, label, alpha=1):
    for i in data.index:
        record = data.loc[i]
        ax = plt.gca()
        ax.text(record[x] * 1.00, record[y], record[label], size='x-small', alpha=alpha)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import time

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
        ax.text(record[x], record[y], record[label], size='x-small', alpha=alpha)

geo_diffs = {'Austin': -.08,
             'Boston': -.01,
             'Charlotte': -.09,
             'Chicago': -.05,  # was -.06
             'Dallas': -.06,
             'Denver': -.06,  # was -.05
             'Los Angeles': .01,
             'New York': .04,  # was .05
             'Phoenix': -.08,  # was -.12, then -.11
             'Portland': -.05,  # was -.08, then -.07
             'San Francisco': .07,  # was .08
             'Seattle': 0}

def test():
    while True:
        pyautogui.moveTo(1500, 1000, 2)
        pyautogui.click()
        time.sleep(10)
        pyautogui.moveTo(1700, 1000, 2)
        pyautogui.click()
        time.sleep(10)

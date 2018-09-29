import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_people(file):
    df = pd.read_csv(file)
    print(df.columns)

    f, ax = plt.subplots(2)
    ax[0].plot(df['age'], df['weight'], label='age')
    ax[0].legend()
    #plt.plot(df['weight'], label='weight')
    ax[1].scatter(df['age'], df['weight'])
    ax[1].legend()
    plt.show()


def run_weather(file):
    df = pd.read_csv(file, parse_dates=[0], index_col=0)
    print(df.columns)
    df.plot(xticks=df.index)
    plt.show()


if __name__ == '__main__':
    file_name = 'people.csv'
    file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    #run_people(file=file_path)


    file_name = 'weather.csv'
    file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    run_weather(file=file_path)
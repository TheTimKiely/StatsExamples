import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_people(file):
    df = pd.read_csv(file)
    print(df.columns)

    histogram = {}
    histogram['20s'] = len([p for p in df['age'] if int(p/10) == 2])
    histogram['30s'] = len([p for p in df['age'] if int(p/10) == 3])
    histogram['40s'] = len([p for p in df['age'] if int(p/10) == 4])
    histogram['50s'] = len([p for p in df['age'] if int(p/10) == 5])
    histogram['60s'] = len([p for p in df['age'] if int(p/10) == 6])
    histogram['70s'] = len([p for p in df['age'] if int(p/10) == 7])
    histogram['80s'] = len([p for p in df['age'] if int(p/10) == 8])

    plt.bar(list(histogram.values()))
    #plt.hist(list(histogram.values()), bins=len(histogram))
    plt.ylabel('People')

    #sns.distplot([2,3,6,8,6,4,1])
    #sns.distplot(list(histogram.values()), bins=len(histogram))

    # n, bins, patches = plt.hist(list(histogram.values()), len(histogram))
    # plt.plot(bins, xticks=list(histogram.keys()))
    # plt.show()
    # f, ax = plt.subplots(2)
    # ax[0].plot(df['age'], df['weight'], label='age')
    # ax[0].legend()
    # #plt.plot(df['weight'], label='weight')
    # ax[1].scatter(df['age'], df['weight'])
    # ax[1].legend()
    plt.show()

def run_weather(file):
    df = pd.read_csv(file, parse_dates=[0], index_col=0)
    print(df.columns)
    #observation = df['2018-07-31 19:00:00']
    df.plot(xticks=df.index)
    plt.show()


def run_hockey(file):
    df = pd.read_csv(file, header=1)
    print(df.columns)
    print(df.shape)
    print(df['Player'])

    plt.plot(df['PTS'], xticks=df['Player'])
    plt.show()


if __name__ == '__main__':
    file_name = 'people.csv'
    file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    #run_people(file=file_path)


    file_name = 'weather.csv'
    file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    #run_weather(file=file_path)


    file_name = 'RedWings2018.csv'
    file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
    run_hockey(file=file_path)

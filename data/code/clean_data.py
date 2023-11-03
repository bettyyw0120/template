import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


### DEFINE
def main():
    df = pd.read_csv('output/data_merged.csv')
    plot_data(df)
    df = clean_data(df)
    df.to_csv('output/data_cleaned.csv', index = False)

"""
def plot_data(df):
    plt.hist(df['chips_sold'])
    plt.savefig('output/chips_sold.pdf')
"""
def to_percent(y, position):
    s = "{:.0f}%".format(y)
    return s

def plot_data(df):
    weights = (1 / df['chips_sold'].count()) * 100 * np.ones_like(df['chips_sold'])
    plt.hist(df['chips_sold'], weights = weights)
    formatter = FuncFormatter(to_percent)
    plt.gca().yaxis.set_major_formatter(formatter)
    plt.savefig('output/chips_sold.pdf')

def clean_data(df):
    df['chips_sold'][df['chips_sold'] == -999999] = np.NaN
    return(df)
    
### EXECUTE
main()

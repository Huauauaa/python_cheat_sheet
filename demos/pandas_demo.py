import pandas as pd
import numpy as np

# https://pandas.pydata.org/

data = pd.read_csv('data/index.csv')
s = pd.Series([1, 2, 3, np.nan, 3, 6, 9])


def main():
    print(data)
    print(s)


if __name__ == '__main__':
    main()

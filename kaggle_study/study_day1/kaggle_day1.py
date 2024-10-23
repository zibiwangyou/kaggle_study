import pandas as pd


def process():
    path = r'../files/data.csv'
    df = pd.read_csv(path, encoding='ISO-8859-1', dtype={'CustomerID': str})
    print(df.info())


if __name__ == '__main__':
    process()
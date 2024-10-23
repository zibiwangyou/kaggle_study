import pandas as pd


def process():
    path = r'../files/data.csv'
    df = pd.read_csv(path, encoding='ISO-8859-1', dtype={'CustomerID': str})
    print(df.info())
    print(df.shape)

    # 缺失值统计：
    na_count = df.apply(lambda x: sum(x.isnull()/len(x)), axis=0)
    print(na_count)


if __name__ == '__main__':
    process()
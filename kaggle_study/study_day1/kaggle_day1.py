# -*- encoding: utf-8 -*-
"""
    学习链接：
    https://blog.csdn.net/qq_44186838/article/details/120548206?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522C3EDBB01-1BBB-4ADB-95BC-7CEDA37A9CA8%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=C3EDBB01-1BBB-4ADB-95BC-7CEDA37A9CA8&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-5-120548206-null-null.142^v100^pc_search_result_base6&utm_term=kaggle%E9%A1%B9%E7%9B%AE%E5%AE%9E%E6%88%98&spm=1018.2226.3001.4187
"""
import pandas as pd


def process_data_clean():
    path = r'../files/data.csv'
    df = pd.read_csv(path, encoding='ISO-8859-1', dtype={'CustomerID': str})

    """
    步骤一: 检查数据维度和基本情况
    """
    print(df.info())
    print(df.shape)

    """
    步骤二: 缺失值处理
    填充缺失值的方法：
    1. 直接指定默认值：fillna('XXX')，
    2. 用前一个有效值填充：fillna('method'='ffill')
    3. 用后一个有效值填充：fillna('method'= 'bfill')
    4. 用平均数/中位数/众数填充： fillna(df.mean()/df.median()/df.mode().iloc[0])
    """
    # 缺失值统计：
    na_count = df.apply(lambda x: (sum(x.isnull()) / len(x)), axis=0)
    print(na_count)

    # 发现产品描述（Description）和 顾客id两列有缺失值，全部填充为各自的默认值：
    df['Description'] = df['Description'].fillna('missing desc').astype('str')
    df['CustomerID'] = df['CustomerID'].fillna('Unknown').astype('str')
    print(df.info())

    # 缺失值统计2，此刻所有字段都有值，缺失值处理完成
    na_count2 = df.apply(lambda x: (sum(x.isnull()) / len(x)), axis=0)
    print(na_count2)

    """
    步骤三：日期格式转换，
    1. 用pandas的to_datetime方法把字段转换成 pandas的日期时间格式（datetime64[ns] 类型）；
    2. 再用 .dt方法， 访问日期和时间的组件，再调用具体的 strftime 方法，并传入需要的时间格式即可
    """
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']).dt.strftime('%Y-%m-%d')
    print(df['InvoiceDate'])

    """
    步骤四：去重
    """
    df = df.drop_duplicates()
    print(df.shape)

    """
    步骤五：异常值处理
    在这个场景中，我们把退货的订单看作是异常值，也就是【数量为负数】或者【货单价为负数】
    1. 查看有多少这类数据；
    2. 过滤或直接删除这类数据；
    """
    print(df.columns)

    # 检查当前df中，数量或货单价 之一 有负数的情况
    df_abnormal = df[(df['Quantity'] < 0) | (df['UnitPrice'] < 0)]
    print(df_abnormal[['InvoiceNo', 'Quantity', 'UnitPrice']])

    # 直接过滤出两者都大于0的数据
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    print(df.shape)

    writer = pd.ExcelWriter('../files/cleaned_data.xlsx')
    df.to_excel(writer, index=False)
    writer._save()


def process_rfm():
    pass


if __name__ == '__main__':
    process_data_clean()
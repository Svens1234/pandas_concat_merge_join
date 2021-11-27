import numpy as np
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

print(df1)
print(df2)
print(df3)
print(pd.concat([df1, df2, df3]))
print(type(pd.concat([df1, df2, df3])))
print(pd.concat([df1, df2, df3], axis=1))

df4 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [1, 2, 3],
                    'user_name': ['James Brown', 'Jack White', 'Jane Green'],
                    'country': ['USA', 'USA', 'France']})

df5 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [1, 2, 3],
                    'order_date': ['2020-02-11', '2020-02-11', '2020-02-11' ],
                    'OS': ['Android', 'IOS', 'Android']})

print(df4)
print(df5)
print(pd.merge(df4,df5))
print(pd.merge(df4,df5, on='user_id'))
print(pd.merge(df4,df5, on='order_id'))


df6 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [1, 2, 3],
                    'user_name': ['James Brown', 'Jack White', 'Jane Green'],
                    'country': ['USA', 'USA', 'France']})

df7 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [2, 4, 5],
                    'order_date': ['2020-02-11', '2020-02-11', '2020-02-11' ],
                    'OS': ['Android', 'IOS', 'Android']})

print(df6)
print(df7)
print(pd.merge(df6,df7))
print(pd.merge(df6,df7, on='user_id'))
print(pd.merge(df6,df7, on=['user_id', 'order_id']))


df8 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [1, 2, 3],
                    'user_name': ['James Brown', 'Jack White', 'Jane Green'],
                    'country': ['USA', 'USA', 'France']})

df9 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [2, 4, 3],
                    'order_date': ['2020-02-11', '2020-02-11', '2020-02-11' ],
                    'OS': ['Android', 'IOS', 'Android']})

print(df8)
print(df9)
print(pd.merge(df8, df9))
print(pd.merge(df8, df9, on='user_id'))
print(pd.merge(df8, df9, on=['user_id', 'order_id']))


df9 = pd.DataFrame({
                    'user_name': ['James Brown', 'Jack White', 'Jane Green'],
                    'country': ['USA', 'USA', 'France']},
                   index=['ind1', 'ind2', 'ind3'])

df10 = pd.DataFrame({'order_id': [114, 235, 432],
                    'user_id': [2, 4, 3],
                    'order_date': ['2020-02-11', '2020-02-11', '2020-02-11' ],
                    'OS': ['Android', 'IOS', 'Android']},
                    index=['ind1', 'ind4', 'ind3'])

print(df9)
print(df10)
print(df9.join(df10))
print(df10.join(df9))

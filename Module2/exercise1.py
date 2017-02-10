#load data

import pandas as pd
df = pd.read_csv('direct_marketing.csv')

#from sqlalchemy import create_engine
#engine = create_engine('sqlite:///:memory:')
#
#
#sql_dataframe  = pd.read_sql_table('my_table', engine, columns=['ColA', 'ColB'])
#xls_dataframe  = pd.read_excel('my_dataset.xlsx', 'Sheet1', na_values=['NA', '?'])
#json_dataframe = pd.read_json('my_dataset.json', orient='columns')
#csv_dataframe  = pd.read_csv('my_dataset.csv', sep=',')
#table_dataframe= pd.read_html('http://page.com/with/table.html')[0]

#df.columns = ['new', 'column', 'header', 'labels']

#不同的调用方式
print(df.columns)
#print(df.head(5))
#print(df.head(5).recency)
#print(df.head(5)['recency'])
#print(df.head(5)[['recency']])
print(df.loc[0:4, 'recency'])
#print(df.loc[0:4, ['recency']])
print(df.iloc[0:5, 0])
#print(df.iloc[0:5, [0]])
#print(df.ix[0:5, 0])


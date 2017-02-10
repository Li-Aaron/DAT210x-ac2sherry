#astype & cat

import pandas as pd

income_ordered = ['$1 - $1000',
                  '$1000 - $10000',
                  '$10000 - $50000',
                  '$50000 - $100000',
                  '+$100000']

df = pd.DataFrame({
                   'income':[
                          '$10000 - $50000',
                          '$50000 - $100000',
                          '+$100000',
                          '$1 - $1000',
                          '$1000 - $10000',
                          '$10000 - $50000',
                          '$50000 - $100000',
                          '+$100000',
                          '+$100000']})

print(df)

#df.income = df.income.astype("category",
#                             ordered = True,
#                             categories = income_ordered).cat.codes
#                             
#print(df)

df.income = df.income.astype("category").cat.codes
                                 
                             
print(df)

df = pd.get_dummies(df,columns=['income'])

print(df)


import pandas as pd
#import html5lib as html5lib

# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
#df = pd.read_html('http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')
htmlstr = 'http://espn.go.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2'
df = pd.read_html(htmlstr)[0]
columns = df.iloc[1,:]
df.columns = columns
col_num = len(columns)
df_1 = df.dropna(thresh = col_num-4) # drop最少4个NAN的值
df_1 = df_1.drop(df.RK == 'RK')
#df_1 = df_1[(df.RK != 'RK')]
#df_1 = df_1.iloc[:,1:]
df_1.iloc[:,1] = pd.to_numeric(df.iloc[:,1],errors='coerce');
print(df_1.describe())
#print(df_1.loc[15:16,'GP'])

#df_not = df[(df.PLAYER != 'PP') & (df.TEAM != 'SH')]

# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..


# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..


# TODO: Get rid of the 'RK' column
#
# .. your code here ..


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..



# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric



# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.


import pandas as pd
#from collections import Counter

# TODO: Load up the dataset
# Ensuring you set the appropriate header column names
#
# .. your code here ..

df = pd.read_csv("Datasets/servo.data",header=None)
df.columns = ['motor', 'svrew', 'pgain', 'vgain', 'class']

# TODO: Create a slice that contains all entries
# having a vgain equal to 5. Then print the 
# length of (# of samples in) that slice:
#
# .. your code here ..

df_a = df[df.vgain == 5]
#print(Counter(df.vgain == 5))

# TODO: Create a slice that contains all entries
# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..

df_b = df[(df.motor == 'E') & (df.svrew == 'E')]
#print(Counter((df.motor == 'E') & (df.svrew == 'E')))


# TODO: Create a slice that contains all entries
# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..

df_c = df[df.pgain == 4]
print(df_c.describe())


# TODO: (Bonus) See what happens when you run
# the .dtypes method on your dataframe!
print(df.dtypes)



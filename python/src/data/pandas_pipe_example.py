import pandas as pd
df=pd.DataFrame({
    'order':range(5),
    'alphabet':['a','b','c','d','e']
})

# assign new column to the processing dataframe then count its value
(
    df
    .pipe(lambda x: x.assign(is_a=x.alphabet=='a'))
    .groupby(['is_a'])
    .count()
    .iloc[:,:1]
    .reset_index()
)
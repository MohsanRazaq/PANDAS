import pandas as pd
list={
    'ID':[1,2,3,4],
    'Name':['Ali', 'Ahsan', 'Mohsan', 'Ahmad ','noni'],
    'Marks':[60, 85, 95, 70 ]
    
}
df=pd.DataFrame(list)
pd=df.set_index('ID')
print(df.loc[df['Name'] == 'Mohsan', 'Marks'])

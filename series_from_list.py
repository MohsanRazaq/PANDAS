import pandas as pd
## list of names
names=['mohsan','ahsan','ali','ahmad','moeez']
res=pd.Series(names)
print(f'With default Index:/n{res}')
res=pd.Series(names)
print(f'WithOUT  default Index:/n{res.to_string(index=False)}')
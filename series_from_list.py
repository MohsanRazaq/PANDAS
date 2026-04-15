import pandas as pd

names = ['mohsan','ahsan','ali','ahmad','moeez']
res=(pd.Series(names))
#with def index
print(f'With index(Default)\n{res}')
# with custom index, no index
print(f' With custome index(No Index)\n{res.to_string(index=False)}')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv(r'E:\工作\学习\python\shop_anaysis\11207483_data.csv') 

#df.info()

df1=df.dropna(how='any')
df1.info()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data=pd.read_csv('./new_data.csv')
print(data.groupby(['gender','usertype'])['bikeid'].count())
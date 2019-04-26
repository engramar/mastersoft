import pandas as pd
import numpy as np

df = pd.read_csv("raLEGACY.log", header=None, delimiter="|")
df2 = pd.pivot_table(df, index=[0], columns=[1], aggfunc=len)
df2.head(1000).to_csv('raLEGACY.csv')

#Reference: https://pypi.python.org/pypi/pandas-profiling
import pandas as pd
import pandas_profiling
import numpy as np

if __name__ ==  '__main__':
	df=pd.read_csv("D:\meteorite\Meteorite_Landings.csv", parse_dates=['year'], encoding='UTF-8')
	pfr = pandas_profiling.ProfileReport(df)
	pfr.to_file("D:\meteorite\meteorite.html")

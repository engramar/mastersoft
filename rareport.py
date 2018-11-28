import mysql.connector
import datetime
import pandas as pd
import numpy as np

mydb = mysql.connector.connect(
  host="win10-mysql-tst",
  user="root",
  passwd="root",
  #database="rightaddress"
  database="simplicity_rightaddress_new"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT DisplayValue, CreatedOn FROM executionlog where Organisation_RSN = 'DB03CEC2-F91E-40B0-A6D4-E046253BAA29'")
myresult = mycursor.fetchall()

for row in myresult :
	method = row[0]
	month = row[1].strftime('%Y-%m')	
	print (method+"|"+month)

df = pd.read_csv("raLEGACY.log", header=None, delimiter="|")
df2 = pd.pivot_table(df, index=[0], columns=[1], aggfunc=len)
df2.head(1000).to_csv('raLEGACY.csv')
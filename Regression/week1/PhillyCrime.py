# pure python code
import graphlab
import pandas as pd
import os

# os.chdir('C:\project\personal\ZhenCouseraML\Regression\week1')
sales = graphlab.SFrame.read_csv('Philadelphia_Crime_Rate_noNA.csv/')
sales.header(4)

pd_sales=pd.read_csv('Philadelphia_Crime_Rate_noNA.csv')

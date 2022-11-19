import os
from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl
import statistics

dfr = pd.read_excel('data.xlsx')
X = ['Subject1','Subject2','Subject3','SUbejct4', 'Subejct5']
maximum_marks = [
	dfr['Subject1'].max(),
	dfr['Subject2'].max(),
	dfr['Subject3'].max(),
	dfr['Subject4'].max(),
	dfr['Subject5'].max(),
	]
minimum_marks = [
	dfr['Subject1'].min(),
	dfr['Subject2'].min(),
	dfr['Subject3'].min(),
	dfr['Subject4'].min(),
	dfr['Subject5'].min(),
]
you_marks = [20,30,25,30,80]

X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, maximum_marks, 0.2, label = 'Max-marks')
plt.bar(X_axis + 0.2, minimum_marks, 0.2, label = 'Min-marks')
plt.bar(X_axis, you_marks, 0.2, label = 'Your-marks')
  
plt.xticks(X_axis, X)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Report")
plt.legend(loc='upper left')
plt.show()
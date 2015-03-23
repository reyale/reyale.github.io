import pandas as pd

def save_as(ax, file_name, xlabel, ylabel):
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  fig = ax.get_figure()
  fig.savefig(file_name)

data = pd.read_csv('Current_Employee_Names__Salaries__and_Position_Titles.csv')
data['Employee Annual Salary'] = data['Employee Annual Salary'].apply(lambda x : x.replace('$',''))
data['Employee Annual Salary'] = data['Employee Annual Salary'].astype('float')
save_as(data['Employee Annual Salary'].hist(), './chicago_salary_hist.png', 'salary', 'count')


import pandas as pd
import datetime
import matplotlib.pyplot as plt

seconds_in_month = 60 * 60 * 24 * 30

def save_as(ax, file_name, xlabel, ylabel):
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  fig = ax.get_figure()
  fig.savefig(file_name)
  plt.close()

data = pd.read_csv('jerseycitypublicemployeeswithtitlesandhiredates20feb2014.csv', encoding='utf-8')
data['SALARY'] = data['SALARY'].apply(lambda x : x.replace('$','').replace(',',''))
data['SALARY'] = data['SALARY'].astype('float')

print data['SALARY'].describe()
save_as(data['SALARY'].hist(), 'jcsalary_hist.png','salary','count')

def hist_salary_plot(df):
  plt.hist(df['SALARY'], alpha=0.5) 
data.groupby('DPT').apply(func=hist_salary_plot)
ax = plt.gca()
ax.set_xlabel('salary')
ax.set_ylabel('count')
plt.savefig('salaries_by_dpt_historgram.png')
plt.close()

now = datetime.datetime.now()
has_hire_date  = data[pd.notnull(data['HIREDATE'])]
has_hire_date['HIREDATE'] = has_hire_date['HIREDATE'].apply(lambda x : (now-datetime.datetime.strptime(x,'%m/%d/%y')).total_seconds()/ seconds_in_month)

save_as(has_hire_date['HIREDATE'].hist(), './hiretime_hist.png','time months','count')

print has_hire_date['HIREDATE'].describe()
print has_hire_date['HIREDATE'].corr(has_hire_date['SALARY'])
print has_hire_date.groupby('DPT').apply(lambda x : x['HIREDATE'].corr(x['SALARY']))
print has_hire_date.groupby('DPT')['HIREDATE'].describe()

def scatter_show(df):
  copied_df = df.copy().reset_index()
  dept_name = copied_df['DPT'].iget(0)
  plt.plot(copied_df['HIREDATE'],copied_df['SALARY'], marker='o', linestyle='', ms=12, label=dept_name)
has_hire_date.groupby('DPT').apply(func=scatter_show)

#plt.legend()
ax = plt.gca()
ax.set_xlabel('time months')
ax.set_ylabel('salary')
plt.savefig('salary_by_time_by_dept.png')

#who is in the upper left?
print has_hire_date.irow((has_hire_date['SALARY']/has_hire_date['HIREDATE']).argmax())

print data.groupby('DPT').apply(lambda x : x['SALARY'].mean())

#best place to work
print has_hire_date.groupby('DPT').apply(lambda x : x['SALARY'].mean()/x['HIREDATE'].mean())

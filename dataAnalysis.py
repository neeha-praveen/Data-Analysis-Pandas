import pandas as pd
import matplotlib.pyplot as plt # data visualization
import seaborn as sb # heatmap

df = pd.read_csv('data.csv')

# displays the first five rows of the data file
print(df.head())

# describes the numerical data with statistics
print(df.describe())

# finds missing values in each column
missingVal = df.isnull().sum()
print("missing values in each column: \n", missingVal)

# calculates the average of a column
avg = df['Age'].mean()
print(f"average of age: {avg}")

# counts the number of unique values in a column
unique = df['Age'].nunique()
print(f"unique values: {unique}")

# filters rows based on a condition
dev = df[df['Department']=='Development']
print(f"employees working in development:\n",dev)

# find max
max_salary = df['Salary'].max()
max_salary_emp = df[df['Salary']==max_salary]
print(f"highest paid employee: \n {max_salary_emp}")

# counts frequency of each value in a column
emp_dept_count = df['Department'].value_counts()
print(f"no. of employees in each department: \n {emp_dept_count}")

# sorts data by column
sort = df.sort_values(by='Age', ascending=False)
print(f"Sorted by age: \n {sort}")

# adds new column based on condition
df['Experience'] = df['Age'].apply(lambda x: 'Senior' if x>30 else 'Junior')
print("data w experience column: \n",df)


# data visualization using matplotlib

# 1 row 2 columns
fig,axes = plt.subplots(2,2,figsize=(16,6))

# pie graph
axes[0,0].pie(emp_dept_count, labels=emp_dept_count.index, autopct='%1.1f%%', startangle=140)
axes[0,0].set_title("Departments")

# bar graph
axes[0,1].bar(emp_dept_count.index, emp_dept_count.values)
axes[0,1].set_xlabel('Department')
axes[0,1].set_ylabel('Employees')
axes[0,1].set_yticks(emp_dept_count.values)

# scatter graph
axes[1,0].scatter(emp_dept_count.index, emp_dept_count.values, color = 'red')
axes[1,0].set_xlabel('Department')
axes[1,0].set_ylabel('Employees')
axes[1,0].set_yticks(emp_dept_count.values)

# heat map
heatmap_data = emp_dept_count.reset_index()
heatmap_data.columns = ['Department', 'Count']
heatmap_df = pd.DataFrame({'Department': heatmap_data['Department'], 'Count': heatmap_data['Count']}).set_index('Department')
sb.heatmap(heatmap_df, annot=True, cmap='coolwarm', fmt='.0f', cbar=False, ax=axes[1, 1])

plt.tight_layout()
plt.show()
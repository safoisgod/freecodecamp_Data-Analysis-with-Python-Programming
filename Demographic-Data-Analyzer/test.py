import pandas as pd


pd.set_option("display.max_rows",10)


df=pd.read_csv("adult.data.csv")
print(df)
#print(df["race"].unique())
print(df["race"].value_counts())

#print(df["sex"].unique())
#print(df[df["sex"]=="Male"]["age"].mean())
print(df["education"].value_counts())

print((df[df["education"]=="Bachelors"])["education"].value_counts())
#print(df[df["education"]=="Bachelors"].value_counts())


higher_education = df[df["education-num"]>=13]
lower_education = df[df["education-num"]<13]

# percentage with salary >50K
higher_education_rich = higher_education[higher_education["salary"]==">50K"].shape[0]/df.shape[0]*100
lower_education_rich = lower_education[lower_education["salary"]==">50K"].shape[0]/df.shape[0]*100

print(higher_education_rich)
print(lower_education_rich)

print(df["hours-per-week"].min())
print(df["hours-per-week"].max())

min_work_hours = df["hours-per-week"].min()
num_min_workers = df[(df["salary"]==">50K")&(df["hours-per-week"]==min_work_hours)].shape[0]
rich_percentage = (num_min_workers/df.shape[0])*100
print(rich_percentage)

higher_education = ['Bachelors', 'Masters', 'Doctorate']
higher_education = df[df['education'].isin(higher_education)]
print(higher_education.shape[0])
    
mask = df['education'].isin(['Bachelors','Masters','Doctorate'])
lower_education = df[~mask]

    # percentage with salary >50K
huge_salary = higher_education[higher_education['salary'] == '>50K']
print(huge_salary.shape[0])
higher_education_rich = round((len(huge_salary)/len(higher_education)) * 100, 1)
print(huge_salary.shape[0]/higher_education.shape[0])
print(higher_education_rich)

lower_education_salary = len(lower_education[lower_education['salary'] == '>50K'])
lower_education_rich = round((lower_education_salary/len(lower_education)) * 100, 1)
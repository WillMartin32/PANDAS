from numpy import fabs
import pandas as pd

grades_dict = {
    "Wally": [87, 96, 70],
    "Eva": [100, 87, 90],
    "Sam": [94, 77, 90],
    "Katie": [100, 81, 82],
    "Bob": [83, 65, 85],
}

grades = pd.DataFrame(grades_dict)

grades.index = ["Test1", "Test2", "Test3"]

print(grades)

# print(grades["Eva"])

# print(grades.Sam)

# using the loc and iloc methods

#print(grades.loc["Test2"])

#print(grades.iloc[1])

# For consecutive rows
#print(grades.loc["Test1":"Test3"])
#print(grades.iloc[0:3])

#For non-consecutive rows
#print(grades.loc[['Test1','Test3']])
#print(grades.iloc[[0,2]])

#View only Eva's and Katie's grades for Test1 and Test2
print(grades.loc[:'Test2',['Eva','Katie']])

#View only Sam's THRU BOB's grades for Test1 and Test3
print(grades.loc[['Test1','Test3'], 'Sam':'Bob'])

#Select everyone with an A grade
grades_A = grades[grades>=90]

print(grades_A)

#Create a dataframe for everyone with a B grade
grades_B = [(grades>=80) & (grades < 90)]
print(grades_B)

#Create a dataframe for everyone with an A or B grade

grades_A_or_B = [(grades>=90) | (grades>=80)] # | means or

print(grades_A_or_B)

pd.set_option('precision', 2)

print(grades.T.describe())


print(grades.sort_index(ascending=False))

print(grades.sort_index(axis=1,ascending=False))


print(grades.sort_values(by='Test1', axis=1, ascending=False))

print(grades.T.sort_values(by='Test1', ascending=False))


print(grades.loc['Test1'].sort_values(ascending=False))
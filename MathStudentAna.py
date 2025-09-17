import pandas as pd

StudentData = pd.read_csv ('PLP python assignments/student-mat.csv', sep=';')

# display the first few rows of the dataset
firstRows = StudentData.head()
print (firstRows)

#number of rows and columns
#print (StudentData.shape)

#list ofcolumn names
#print (StudentData.columns)

# count missing values in each column
#print(StudentData.isnull().sum())

# check if there are missing values anywhere in the dataset
#print(StudentData.isnull().values.any())

#to check the datatype in each column
#print(StudentData.dtypes)


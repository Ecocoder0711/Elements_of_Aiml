import pandas as pd

# Create a clean dataset
data = {
    'Name' : ['Alice','Bob','Charlie','David','Eva'],
    'Age' : [24,27,22,32,29],
    'Salary' : [50000,54000,50000,58000,52000],
    'Department' : ['HR','Engineering','HR','Engineering','Marketing']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a csv file
df.to_csv('clean_data.csv',index = False)

# Load the clean csv file 

data = pd.read_csv('clean_data.csv')

#Display the loaded data 

print(data)

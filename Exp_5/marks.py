import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Student_Marks.csv')

sns.countplot(x='ROLL NO',data = data)
plt.title('ROLL NO')
plt.show()

sns.countplot(x= 'MARKS',data = data)
plt.title('MARKS')
plt.show()



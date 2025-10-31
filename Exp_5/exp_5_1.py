# code to print fisrt five rows

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

data = pd.read_csv("StressLevelDataset.csv")

sns.countplot(x='anxiety_level', data=data.head())
plt.title('Anxiety Level Distribution')
plt.show()

sns.countplot(x='self_esteem', data=data.head())
plt.title('self_esteem Distribution')
plt.show()

sns.countplot(x='depression', data=data.head())
plt.title('depression Distribution')
plt.show()

sns.heatmap(data[['blood_pressure', 'sleep_quality']].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Cars_Datasets_2025.csv',  encoding='latin1')

sns.countplot(x='Company Names',data = data)
plt.title('Company Names')
plt.show()

sns.countplot(x= 'Cars Names',data = data)
plt.title('Cars Names')
plt.show()

sns.countplot(x = 'Engines', data = data)
plt.title('Engines')
plt.show()

sns.heatmap(data[['Company Names','Cars Names']].corr(),annot=True,cbar='coolware',linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


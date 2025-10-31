import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('Iris.csv')

sns.countplot(x='Id',data = data)
plt.title('Id')
plt.show()

sns.countplot(x= 'SepalLengthCm',data = data)
plt.title('SepalLengthCm')
plt.show()

sns.countplot(x = 'SepalWidthCm', data = data)
plt.title('SepalWidthCm')
plt.show()

sns.heatmap(data[['Id','SepalLengthCm']].corr(),annot=True,cbar='coolware',linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()


# split data
import pandas as pd
from sklearn.model_selection import train_test_split
from pandas import DataFrame

data = pd.read_csv('C:\Users\dancingm\Desktop/Ionosphere.csv')
print data.head()
y = data.Class
X = data.drop('Class', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

df_train_x = DataFrame(X_train)
df_train_y = DataFrame(y_train)
df_train = pd.concat([df_train_x, df_train_y], axis=1, join_axes=[df_train_x.index])
df_train.to_csv('C:\Users\dancingm\Desktop/iono_train.csv')

df_test_x = DataFrame(X_test)
df_test_y = DataFrame(y_test)
df_test = pd.concat([df_test_x, df_test_y], axis=1, join_axes=[df_test_x.index])
df_test.to_csv('C:\Users\dancingm\Desktop/iono_test.csv')

print("\nX_train:\n")
print(X_train.head())
print(X_train.shape)

print("\nY_train:\n")
print(y_train.head())
print(y_train.shape)

print("\nX_test:\n")
print(X_test.head())
print(X_test.shape)
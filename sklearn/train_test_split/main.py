from sklearn import datasets
from sklearn.model_selection import train_test_split

data_iris = datasets.load_iris()

x = data_iris.data
y = data_iris.target

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

import joblib
import numpy as np
from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)
print(X_train.shape)
print(X_test.shape)

clf = GradientBoostingClassifier()
clf.fit(X_train, y_train)

print(f'Train Score: {clf.score(X_train, y_train):.2f}')
print(f'Test Score: {clf.score(X_test, y_test):.2f}')

# Store Model
filename = 'models/mnist.pkl'
joblib.dump(clf, filename, compress=9)

# Store Test Data
np.savetxt('data/X_test.txt', X_test, fmt='%d')
np.savetxt('data/y_test.txt', y_test, fmt='%d')

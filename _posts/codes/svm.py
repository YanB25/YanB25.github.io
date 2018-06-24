from sklearn import datasets
dataset = datasets.make_classification(n_samples=1000, n_features=10, n_informative = 8, n_redundant=2, n_repeated=0, n_classes=4)
kf = cross_validation.KFold(n, n_folds=10, shuffle=True)
for train_index, test_index in kf:
    X_train, y_train = dataset[0][train_index], dataset[0]
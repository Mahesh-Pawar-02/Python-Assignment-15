import pandas as pd
from sklearn import datasets
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def Wine_Predictor():

    # wine = pd.read_csv(Path)

    wine = datasets.load_wine()

    print(wine.feature_names)
    print(wine.target_names)

    print(wine.data[0:5])

    print(wine.target)

    X_train, X_test, Y_train, Y_test = train_test_split(wine.data, wine.target, test_size=0.3)

    KNN = KNeighborsClassifier(n_neighbors=3)

    KNN.fit(X_train, Y_train)
    Y_Pred = KNN.predict(X_test)

    print("Accuracy : ",metrics.accuracy_score(Y_test, Y_Pred))

def main():
        print("------------Created By Mahesh Pawar-------------")

        print('Machine Learning Application')

        print("Wine Predictor using K Knighbor algorithm")

        Wine_Predictor(Path="WinePredictor.csv")

if __name__ == "__main__":
    main()

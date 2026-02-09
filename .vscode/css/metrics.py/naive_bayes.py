import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    data = {
        'Age': [22, 25, 47, 52, 46, 56, 55],
        'Salary': [25000, 27000, 52000, 58000, 50000, 60000, 62000],
        'Buy': [0, 0, 1, 1, 1, 1, 1]
    }

    df = pd.DataFrame(data)

    X = df[['Age', 'Salary']]
    y = df['Buy']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = GaussianNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nAccuracy:", accuracy_score(y_test, y_pred))

if __name__ == "__main__":
    main()

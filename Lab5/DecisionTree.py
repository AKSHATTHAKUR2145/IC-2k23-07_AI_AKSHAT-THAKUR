"""Decision Tree classifier, evaluation metrics and model persistence."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import pickle

def main():
    df=pd.read_csv("datasets/placement.csv")
    X=pd.get_dummies(df.drop(columns="placed"),drop_first=True)
    y=df["placed"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    model=DecisionTreeClassifier(max_depth=4,random_state=42)
    model.fit(X_train,y_train)
    pred=model.predict(X_test)
    print("Accuracy:",accuracy_score(y_test,pred))
    print("Confusion matrix:\n",confusion_matrix(y_test,pred))
    print("Classification report:\n",classification_report(y_test,pred,zero_division=0))
    plt.figure(figsize=(14,8))
    plot_tree(model,feature_names=X.columns,class_names=["Not placed","Placed"],filled=True)
    plt.tight_layout(); plt.savefig("Lab5/decision_tree.png"); plt.show()
    with open("models/decision_tree.pkl","wb") as f: pickle.dump(model,f)

if __name__=="__main__": main()

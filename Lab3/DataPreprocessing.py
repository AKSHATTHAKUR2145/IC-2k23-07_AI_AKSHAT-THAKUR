"""NumPy/Pandas preprocessing and EDA example."""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess(path="datasets/placement.csv"):
    df=pd.read_csv(path)
    print("Shape:",df.shape)
    print("\nHead:\n",df.head())
    print("\nMissing values:\n",df.isna().sum())
    print("\nSummary:\n",df.describe(include="all"))
    # Missing value handling
    for col in df.select_dtypes(include="number"):
        df[col]=df[col].fillna(df[col].median())
    for col in df.select_dtypes(exclude="number"):
        df[col]=df[col].fillna(df[col].mode().iloc[0])
    # Encode categorical features
    for col in df.select_dtypes(include="object"):
        df[col]=LabelEncoder().fit_transform(df[col].astype(str))
    return df

if __name__=="__main__":
    df=preprocess()
    print("\nProcessed data:\n",df.head())
    X=df.drop(columns=["placed"])
    y=df["placed"]
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
    scaler=StandardScaler()
    X_train=scaler.fit_transform(X_train); X_test=scaler.transform(X_test)
    print("Train/test:",X_train.shape,X_test.shape)

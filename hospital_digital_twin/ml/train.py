import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import joblib
from features import create_features

df = pd.read_csv("data/hospital.csv")

df = create_features(df)

X = df[["er", "icu", "general", "hour", "dayofweek", "rolling_er", "rolling_total"]]
y = df["surge"].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = XGBClassifier(
    n_estimators=150,
    max_depth=4,
    learning_rate=0.1
)

model.fit(X_train, y_train)

joblib.dump(model, "models/xgb_model.json")

print("Model trained.")

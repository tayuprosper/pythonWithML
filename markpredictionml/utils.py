import joblib
import numpy as np
def predict_mark(level,mark1,mark2):
    model = joblib.load("model.pkl")
    params = np.array([[level,mark1,mark2]])
    output = model.predict(params)
    print(output)
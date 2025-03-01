from fastapi import FastAPI
import joblib
import boto3

app = FastAPI()
model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):
    prediction = model.predict([data["features"]])
    return {"prediction": int(prediction[0])}


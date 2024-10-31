import fastapi
import uvicorn
from src.model.model import TitanicModel
from pydantic import BaseModel
import pandas as pd

# define bucket name and model name
bucket_name = "trained-models-omar"
model_name = "titanic_model.pkl"

model = TitanicModel()
model.load_model_from_s3(bucket_name, model_name)

# define server
app = fastapi.FastAPI()


# defines the input scheme
class PredictionRequest(BaseModel):
    sex: str
    age: float
    sibsp: int
    parch: int
    fare: float
    pclass: str


# defines the response scheme
class PredictionResponse(BaseModel):
    survived: int
    probability: float


# define route
@app.get("/")
def home():
    return {"message": "Welcome to the Iris Species Prediction API!"}


# model prediction
@app.post("/predict")
def predict(data: PredictionRequest):

    input_data = pd.DataFrame([data.model_dump().values()], columns=data.model_dump().keys())

    prob = model.predict_proba(input_data)
    prediction = model.predict(input_data)

    return PredictionResponse(survived=prediction[0], probability=prob[0][prediction])


if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)

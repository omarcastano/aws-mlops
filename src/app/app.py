import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import fastapi
import uvicorn

# load iris dataset
data = sns.load_dataset("iris")

# define X and y
X_train, X_test, y_train, y_test = train_test_split(data.drop("species", axis=1), data["species"], test_size=0.2, random_state=42)

# instance logistic regression
model = LogisticRegression()

# fit model
model.fit(X_train, y_train) 

#define server
app = fastapi.FastAPI()

# define route
@app.get("/")
def home():
    return {"message": "Welcome to the Iris Species Prediction API!"}

# show model performance
@app.get("/performance")
def performance():
    accuracy = model.score(X_test, y_test)
    return {"accuracy": accuracy}

# model prediction
@app.post("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    prediction = model.predict_proba([[sepal_length, sepal_width, petal_length, petal_width]])

    return {"prediction": prediction[0]}

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)

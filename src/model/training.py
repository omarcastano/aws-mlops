from src.model.model import TitanicModel
from src.etl.load_data import load_data_from_s3
from loguru import logger

# load data
X_train, X_test, y_train, y_test = load_data_from_s3("omar-mlops-datasets", "titanic.csv")

# train model
model = TitanicModel()
model.fit(X_train, y_train)
logger.info("######## Model trained successfully ########")

## upload model to s3
bucket_name = "trained-models-omar"
model_name = "titanic_model.pkl"

# upload pickled model to s3
model.save_model_in_s3(bucket_name, model_name)

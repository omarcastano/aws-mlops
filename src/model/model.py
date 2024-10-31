from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.impute import SimpleImputer
import pickle
import pandas as pd
import boto3


def get_alone_feature(x):
    """
    Transform the data to get the "alone" feature

    Args:
    -----
        x (pandas.DataFrame): The input data
    """

    return pd.DataFrame((x["sibsp"] + x["parch"]) == 1, columns=["alone"])


class TitanicModel:
    def __init__(self):
        """
        Model that predicts if a passenger survived or not.
        """

        num_preprocessing = Pipeline(steps=[("impute_nulls", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])

        preprocessing = ColumnTransformer(
            transformers=[
                ("get_alone_feature", FunctionTransformer(get_alone_feature), ["sibsp", "parch"]),
                ("ordinal_encoder", OrdinalEncoder(categories=[["male", "female"], ["First", "Second", "Third"]]), ["sex", "pclass"]),
                ("num_prepro", num_preprocessing, ["age", "fare"]),
            ]
        )

        self.model = Pipeline([("preprocessing", preprocessing), ("model", LogisticRegression())])

    def fit(self, X, y):
        """
        Fit the model

        Args:
        -----
            X (pandas.DataFrame): The input data
            y (pandas.Series): The target data
        """

        self.model.fit(X, y)

    def predict(self, X):
        """
        Make predictions

        Args:
        -----
            X (pandas.DataFrame): The input data
        """

        return self.model.predict(X)

    def predict_proba(self, X):
        """
        Predicts probabilities

        Args:
        -----
            X (pandas.DataFrame): The input data
        """

        return self.model.predict_proba(X)

    def save_model_in_s3(self, bucket_name, model_name):
        """
        Save model as pickle

        Args:
        -----

        """

        try:
            s3_client = boto3.client("s3")
            s3_client.put_object(Body=self.pickle_model(), Bucket=bucket_name, Key=model_name)

        except Exception as e:
            print(f"Error uploading model {e}")

    def load_model_from_s3(self, bucket_name, model_name):
        """clea
        Load model from pickle

        Args:
        -----
            file_path (str): The path to load the model from
        """

        try:
            s3_client = boto3.client("s3")
            pickled_model = s3_client.get_object(Bucket=bucket_name, Key=model_name)["Body"].read()
            self.unpickle_model(pickled_model)

        except Exception as e:
            print(f"Error loading model {e}")

    def pickle_model(self):
        """ "Returns the pickled model"""

        return pickle.dumps(self.model)

    def unpickle_model(self, pickled_model):
        """
        Loads the pickled model

        Args:
        -----
            pickled_model (bytes): The pickled model
        """

        self.model = pickle.loads(pickled_model)

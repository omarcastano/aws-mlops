from src.model.model import TitanicModel
from sklearn.pipeline import Pipeline
import numpy as np
import pytest
from moto import mock_aws
import boto3
from unittest.mock import patch


class TestTitanicModel:

    def test_init(self):
        model = TitanicModel()

        assert model.model is not None
        assert isinstance(model.model, Pipeline)

    def test_fit(self, mock_x_and_y):

        X, y = mock_x_and_y
        model = TitanicModel()
        model.fit(X, y)

        assert model.model is not None
        assert isinstance(model.model, Pipeline)

    def test_predict(self, mock_x_and_y, fitted_model):

        X, _ = mock_x_and_y
        y_pred = fitted_model.predict(X)

        assert y_pred.shape[0] == X.shape[0]

    def test_predict_proba(self, mock_x_and_y, fitted_model):

        X, _ = mock_x_and_y
        y_pred_proba = fitted_model.predict_proba(X)

        assert y_pred_proba.shape[0] == X.shape[0]
        assert y_pred_proba.shape[1] == fitted_model.model.classes_.shape[0]

    @mock_aws
    def test_save_and_load_model_s3(self, mock_x_and_y, fitted_model):

        conn = boto3.client("s3", region_name="us-east-1")

        # We need to create the bucket since this is all in Moto's 'virtual' AWS account
        conn.create_bucket(Bucket="mybucket")

        # save model
        fitted_model.save_model_in_s3("mybucket", "model.pkl")

        # load model
        new_model = TitanicModel()
        new_model.load_model_from_s3("mybucket", "model.pkl")

        X, y = mock_x_and_y

        assert (new_model.predict(X) == fitted_model.predict(X)).all()

    @mock_aws
    def test_save_model_in_s3_handle_error(self, fitted_model, capfd):

        # Simulate a permission error using patch
        with patch("src.model.model.boto3.client") as mock_boto_client:
            mock_boto_client.return_value.put_object.side_effect = Exception("Access Denied")

            fitted_model.save_model_in_s3("mybucket", "model.pkl")

            # Capture printed output
            captured = capfd.readouterr()

            assert "Error uploading model" in captured.out
            assert "Access Denied" in captured.out

    @mock_aws
    def test_load_model_from_s3_handle_error(self, capfd):

        new_model = TitanicModel()
        new_model.load_model_from_s3("mybucket", "model.pkl")

        captured = capfd.readouterr()

        assert "Error loading model" in captured.out

    def test_pickle_and_unpickle_model(self, mock_x_and_y, fitted_model):

        X, _ = mock_x_and_y

        pickle_model = fitted_model.pickle_model()
        new_model = TitanicModel()
        new_model.unpickle_model(pickle_model)

        assert (new_model.predict(X) == fitted_model.predict(X)).all()

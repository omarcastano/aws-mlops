from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import pytest
from src.model.model import TitanicModel
import boto3
from moto import mock_aws


# fixture for the FastAPI client
@pytest.fixture
@patch("src.model.model.boto3")
@patch("src.model.model.TitanicModel")
def client(mock_model, mock_boto, fitted_model):

    mock_model.return_value = fitted_model

    from src.app.app import app

    return TestClient(app)


# test get method
def test_get_home(client):

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Iris Species Prediction API!"}


# test post method
def test_post_predict(client, mock_x_and_y):

    X, _ = mock_x_and_y
    X = X.iloc[0].to_dict()

    response = client.post("/predict", json=X)

    assert response.status_code == 200
    assert isinstance(response.json()["survived"], int)
    assert isinstance(response.json()["probability"], float)

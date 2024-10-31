import pytest
import pandas as pd
from src.model.model import TitanicModel


@pytest.fixture
def mock_dataset():

    MOCK_CSV_DATA = pd.DataFrame(
        {
            "survived": [1, 1, 0, 0, 0],
            "sex": ["male", "female", "female", "male", "female"],
            "age": [4.0, 40.0, 30.0, 22.0, 50.0],
            "sibsp": [0, 0, 0, 0, 1],
            "parch": [2, 0, 0, 0, 2],
            "fare": [81.8583, 15.75, 8.6625, 8.05, 23.45],
            "pclass": ["First", "Second", "Third", "Third", "Third"],
        }
    )

    return MOCK_CSV_DATA


@pytest.fixture
def mock_x_and_y(mock_dataset):

    X = mock_dataset.drop("survived", axis=1)
    y = mock_dataset["survived"]
    return X, y


@pytest.fixture
def fitted_model(mock_x_and_y):

    X, y = mock_x_and_y
    model = TitanicModel()
    model.fit(X, y)

    return model

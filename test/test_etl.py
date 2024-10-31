from src.etl.load_data import load_data_from_s3
from unittest.mock import patch


@patch("pandas.read_csv")
def test_load_data_from_s3(mock_read_csv, mock_dataset):

    # set up the mock to return our sample value
    mock_read_csv.return_value = mock_dataset

    # called the load_data_from_s3 function
    X_train, X_test, y_train, y_test = load_data_from_s3("mock_bucket_name", "mock_file_name")

    assert len(X_train) == len(y_train)
    assert len(X_test) == len(y_test)
    assert len(X_train) + len(X_test) == len(mock_dataset)

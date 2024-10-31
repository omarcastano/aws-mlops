import pandas as pd
from sklearn.model_selection import train_test_split


# function that load data from S3
def load_data_from_s3(bucket_name, file_name):
    """
    Load data from an S3 bucket.

    Args:
    -----
        bucket_name (str): The name of the S3 bucket.
        file_name (str): The name of the file to load.

    Returns:
    ---------
        pandas.DataFrame: The loaded data.
    """

    # load data from S3
    data = pd.read_csv(f"s3://{bucket_name}/{file_name}")

    # select X and y
    y = data.pop("survived")
    X = data

    # Split data to train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

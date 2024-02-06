import pytest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from ml.data import process_data
from ml.model import train_model


def test_rows_in_dataset():
    """
    # Ensure number of rows in dataset is correct
    """

    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    expected_rows = 32561
    actual_rows = data.shape[0]

    assert actual_rows == expected_rows


def test_cols_in_dataset():
    """
    # Ensure number of columns in dataset is correct
    """

    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    expected_cols = 15
    actual_cols = data.shape[1]

    assert actual_cols == expected_cols


def test_model_type_is_forest_classifier():
    """
    # Ensure the model is a forest_classifier type
    """

    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    # split the provided data to have a train dataset and a test dataset
    # Optional enhancement, use K-fold cross validation instead of a train-test split.
    train, test = train_test_split(data, test_size=0.2)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country"
    ]

    # process the training data.
    X_train, y_train, encoder, lb = process_data(
        # use the train dataset
        # use training=True
        # do not need to pass encoder and lb as input
        train,
        categorical_features=cat_features,
        label='salary',
        training=True
    )

    # train the model on the training dataset
    model = train_model(X_train, y_train)

    assert isinstance(model, RandomForestClassifier)


def test_slice_output_is_not_empty():
    """
    # Ensure the slice_output.txt file is not empty
    """

    with open('slice_output.txt', 'r') as file:
        content = file.read()

    assert len(content) > 0

# tests/test_data_validator.py

import pytest

from src import validate_dataframe


def test_validate_dataframe_removes_invalid_ratings(sample_df):
    # TODO: Set the required and numeric column names.
    required_columns = ["record_id", "rating", "name", "category", "status"]
    numeric_columns = ["record_id", "rating"]
    df = validate_dataframe(sample_df, required_columns, numeric_columns)
    # TODO: Assert that 98 rows remain and all five columns are preserved.
    assert df.shape[0] == 98 and df.shape[1] == 5

def test_validate_dataframe_with_missing_column(sample_df):
    # TODO: Set required_columns to include a nonexistent column.
    required_columns = ["record_id", "rating", "name", "category", "status", "NONEXISTENT"]
    numeric_columns = ["record_id", "rating"]
    with pytest.raises(ValueError):
        validate_dataframe(sample_df, required_columns, numeric_columns)    

    
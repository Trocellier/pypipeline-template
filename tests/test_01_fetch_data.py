# tests/test_01_fetch_data.py ----------------------------------------------- #
# Author: Louis Trocellier
# Description: Unit tests for fetch_data functions.

import pytest
import pandas as pd
import numpy as np

# Functions imports
from scripts.f01_fetch_data import (
    fetch_data_settings,
    fetch_data_execution,
    fetch_data_exports,
)


def test_fetch_data_settings_returns_valid_configuration():
    """Test that fetch_data_settings returns valid default configuration."""
    settings = fetch_data_settings()
    
    assert isinstance(settings, dict)
    assert settings.get("data_source") == "raw_sample"
    assert settings.get("max_records") == 1000


def test_fetch_data_execution_returns_valid_dataframe():
    """Test that fetch_data_execution returns a non-empty DataFrame with expected structure."""
    settings = fetch_data_settings()
    df = fetch_data_execution(settings)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert list(df.columns) == ["id", "timestamp", "value"]
    assert np.issubdtype(df["id"].dtype, np.integer)
    assert np.issubdtype(df["value"].dtype, np.floating)


def test_fetch_data_execution_data_integrity():
    """Test that fetched data has correct structure and values."""
    settings = fetch_data_settings()
    df = fetch_data_execution(settings)
    
    assert df["id"].tolist() == list(range(1, 11))
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])
    
    expected_values = [100 + i * 10 for i in range(10)]
    assert df["value"].tolist() == expected_values


def test_fetch_data_exports_creates_output_file(temp_data_dir):
    """Test that export function creates the output file."""
    settings = fetch_data_settings()
    df = fetch_data_execution(settings)
    
    output_path = temp_data_dir / "01_raw_data.parquet"
    df.to_parquet(output_path, index=False)
    
    assert output_path.exists()
    
    df_read = pd.read_parquet(output_path)
    assert len(df_read) == len(df)
    assert df_read.columns.tolist() == df.columns.tolist()
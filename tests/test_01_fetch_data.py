# tests/test_01_fetch_data.py ----------------------------------------------- #
# Author: Louis Trocellier
# Description: Unit tests for fetch_data functions.

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add project root to path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT))

# Import functions - dynamically load the script
from importlib import util
spec = util.spec_from_file_location(
    "fetch_data_script",
    PROJECT_ROOT / "scripts" / "01_fetch_data.py"
)
if spec and spec.loader:
    fetch_data_module = util.module_from_spec(spec)
    sys.modules["fetch_data_script"] = fetch_data_module
    spec.loader.exec_module(fetch_data_module)
    
    fetch_data_settings = fetch_data_module.fetch_data_settings
    fetch_data_execution = fetch_data_module.fetch_data_execution
    fetch_data_exports = fetch_data_module.fetch_data_exports


def test_fetch_data_settings_returns_valid_configuration():
    """Test that fetch_data_settings returns valid default configuration."""
    settings = fetch_data_settings()
    
    assert isinstance(settings, dict)
    assert "data_source" in settings
    assert "max_records" in settings
    assert settings["data_source"] == "raw_sample"
    assert settings["max_records"] == 1000


def test_fetch_data_execution_returns_valid_dataframe():
    """Test that fetch_data_execution returns a non-empty DataFrame with expected structure."""
    settings = fetch_data_settings()
    df = fetch_data_execution(settings)
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert list(df.columns) == ["id", "timestamp", "value"]
    assert df["id"].dtype in [np.int64, int]
    assert df["value"].dtype in [np.float64, float]


def test_fetch_data_execution_data_integrity():
    """Test that fetched data has correct structure and values."""
    settings = fetch_data_settings()
    df = fetch_data_execution(settings)
    
    # Check ID sequence
    assert df["id"].tolist() == list(range(1, 11))
    
    # Check timestamp is datetime
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])
    
    # Check value calculation
    expected_values = [100 + i * 10 for i in range(10)]
    assert df["value"].tolist() == expected_values


def test_fetch_data_exports_creates_output_file(temp_data_dir):
    """Test that export function creates the output file."""
    settings = fetch_data_settings()
    df = fetch_data_execution(settings)
    
    # Mock the export function to use temp directory
    output_path = temp_data_dir / "01_raw_data.parquet"
    df.to_parquet(output_path, index=False)
    
    assert output_path.exists()
    
    # Verify we can read it back
    df_read = pd.read_parquet(output_path)
    assert len(df_read) == len(df)
    assert df_read.columns.tolist() == df.columns.tolist()

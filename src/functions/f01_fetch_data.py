# src/functions/f01_fetch_data.py ------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 01 - Fetching data.

import pandas as pd
from settings import DATA_DIR, logger

# Functions ----------------------------------------------------------------- #
def fetch_data_settings():
    """Load parameters/settings for data fetching."""
    logger.debug("Loading fetch data settings...")
    return {
        "data_source": "raw_sample",
        "max_records": 1000
    }

def fetch_data_execution(settings):
    """Retrieve data based on settings."""
    logger.debug(f"Fetching data from source: {settings['data_source']}")
    
    # Sample data generation
    data = pd.DataFrame({
        "id": range(1, 11),
        "timestamp": pd.date_range("2024-01-01", periods=10),
        "value": [100 + i * 10 for i in range(10)]
    })
    
    return data

def fetch_data_exports(data):
    """Export raw data to intermediate storage."""
    output_path = DATA_DIR / "01_raw_data.parquet"
    
    logger.debug(f"Exporting raw data to {output_path}")
    data.to_parquet(output_path, index=False)
    logger.info(f"Raw data exported: {len(data)} rows")

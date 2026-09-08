# scripts/01_fetch_data.py --------------------------------------------- #
# Author: Louis Trocellier
# Description: Pipeline step 01 - Fetch data execution.

from src.functions.f01_fetch_data import (
    fetch_data_settings,
    fetch_data_execution,
    fetch_data_exports
)

if __name__ == "__main__":
    # 1. Load step configuration/settings
    settings = fetch_data_settings()
    
    # 2. Retrieve raw data
    data = fetch_data_execution(settings)
    
    # 3. Export data in Parquet format
    fetch_data_exports(data)
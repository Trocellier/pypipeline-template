# scripts/02_process_data.py ---------------------------------------------- #
# Author: Louis Trocellier
# Description: Step 02 - Processing data.

from src.functions.f02_process_data import (
    process_load_raw_data,
    process_data,
    process_export_data
)

if __name__ == "__main__":
    # 1. Load raw data
    raw_data = process_load_raw_data()

    # 2. Process data
    processed_data = process_data(raw_data)

    # 3. Export processed data
    process_export_data(processed_data)
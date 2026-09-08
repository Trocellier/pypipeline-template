# scripts/02_process_data.py ---------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 02 - Processing data.

from loguru import logger
import pandas as pd
from pathlib import Path
from global import config, DATA_DIR

# Execution ------------------------------------------------------------ #
logger.info("Starting step 02: Process data")

def load_raw_data():
    """Load raw data from storage."""
    input_path = DATA_DIR / "01_raw_data.parquet"
    
    logger.debug(f"Loading raw data from {input_path}")
    return pd.read_parquet(input_path)

def process_data(data):
    """Apply data processing steps."""
    logger.debug("Applying data transformations")
    
    # Example processing: add computed columns
    processed_data = data.copy()
    processed_data["value_squared"] = processed_data["value"] ** 2
    processed_data["value_normalized"] = (processed_data["value"] - processed_data["value"].mean()) / processed_data["value"].std()
    
    return processed_data

def export_processed_data(data):
    """Export processed data to storage."""
    output_path = DATA_DIR / "02_processed_data.parquet"
    
    logger.debug(f"Exporting processed data to {output_path}")
    data.to_parquet(output_path, index=False)
    logger.info(f"Processed data exported: {len(data)} rows, {len(data.columns)} columns")

# Main Execution
try:
    raw_data = load_raw_data()
    processed_data = process_data(raw_data)
    export_processed_data(processed_data)
    logger.info("Step 02 completed successfully")
except Exception as e:
    logger.error(f"Step 02 failed: {e}")
    raise

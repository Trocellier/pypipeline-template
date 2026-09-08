# scripts/03_export_results.py -------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 03 - Exporting results.

from loguru import logger
import pandas as pd
from pathlib import Path
from global import config, DATA_DIR, OUTPUTS_DIR

# Execution ------------------------------------------------------------ #
logger.info("Starting step 03: Export results")

def load_processed_data():
    """Load processed data from storage."""
    input_path = DATA_DIR / "02_processed_data.parquet"
    
    logger.debug(f"Loading processed data from {input_path}")
    return pd.read_parquet(input_path)

def generate_summary(data):
    """Generate summary statistics."""
    logger.debug("Generating summary statistics")
    
    summary = pd.DataFrame({
        "metric": ["count", "mean", "std", "min", "max"],
        "value": [
            len(data),
            data["value"].mean(),
            data["value"].std(),
            data["value"].min(),
            data["value"].max()
        ]
    })
    
    return summary

def export_results(summary):
    """Export final results to outputs directory."""
    output_path = OUTPUTS_DIR / "03_final_summary.csv"
    
    logger.debug(f"Exporting results to {output_path}")
    summary.to_csv(output_path, index=False)
    logger.info(f"Results exported to {output_path}")

# Main Execution
try:
    processed_data = load_processed_data()
    summary = generate_summary(processed_data)
    export_results(summary)
    logger.info("Step 03 completed successfully")
except Exception as e:
    logger.error(f"Step 03 failed: {e}")
    raise

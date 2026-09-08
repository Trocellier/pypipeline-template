# scripts/03_export_results.py -------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 03 - Exporting results.

import logging
import pandas as pd
from pathlib import Path
from global import DATA_DIR, OUTPUTS_DIR

# Get logger for this module
logger = logging.getLogger(__name__)

# Execution ------------------------------------------------------------ #
def export_load_processed_data():
    """Load processed data from storage."""
    input_path = DATA_DIR / "02_processed_data.parquet"
    
    logger.debug(f"Loading processed data from {input_path}")
    return pd.read_parquet(input_path)

def export_generate_summary(data):
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
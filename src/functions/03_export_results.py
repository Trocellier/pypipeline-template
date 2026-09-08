# scripts/03_export_results.py -------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 03 - Exporting results.

import logging
import pandas as pd
from pathlib import Path

# Get logger for this module
logger = logging.getLogger(__name__)

# These will be injected by main.py
config = None
DATA_DIR = None
OUTPUTS_DIR = None

# Execution ------------------------------------------------------------ #
def load_processed_data():
    """Load processed data from storage."""
    input_path = DATA_DIR / "02_processed_data.csv"
    
    logger.debug(f"Loading processed data from {input_path}")
    return pd.read_csv(input_path)

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

def execute():
    """Execute step 03."""
    logger.info("Starting step 03: Export results")
    try:
        processed_data = load_processed_data()
        summary = generate_summary(processed_data)
        export_results(summary)
        logger.info("Step 03 completed successfully")
    except Exception as e:
        logger.error(f"Step 03 failed: {e}")
        raise

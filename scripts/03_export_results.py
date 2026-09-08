# scripts/03_export_results.py -------------------------------------------- #
# Author: Louis Trocellier
# Description: Step 03 - Exporting results.

import logging

logger = logging.getLogger(__name__)
logger.info("Starting step 03: Export results")

try:
    from src.functions.export_results import (
        load_processed_data,
        generate_summary,
        export_results
    )
    
    processed_data = load_processed_data()
    summary = generate_summary(processed_data)
    export_results(summary)
    logger.info("Step 03 completed successfully")
except Exception as e:
    logger.error(f"Step 03 failed: {e}")
    raise

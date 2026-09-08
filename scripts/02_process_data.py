# scripts/02_process_data.py ---------------------------------------------- #
# Author: Louis Trocellier
# Description: Step 02 - Processing data.

import logging
from importlib import util

logger = logging.getLogger(__name__)
logger.info("Starting step 02: Process data")

try:
    # Dynamic import for file starting with digit
    spec = util.spec_from_file_location("step02", "src/functions/02_process_data.py")
    step02 = util.module_from_spec(spec)
    spec.loader.exec_module(step02)
    
    raw_data = step02.load_raw_data()
    processed_data = step02.process_data(raw_data)
    step02.export_processed_data(processed_data)
    logger.info("Step 02 completed successfully")
except Exception as e:
    logger.error(f"Step 02 failed: {e}")
    raise

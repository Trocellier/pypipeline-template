# main.py -------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Sequential execution of pipeline scripts with error handling.

import runpy
import sys
from global import logger, pipeline_scripts

logger.info("Starting pipeline execution...")

for script in pipeline_scripts:
    logger.info(f"Running script: {script.name}")
    try:
        runpy.run_path(str(script), run_name="__main__")
    except Exception as e:
        logger.error(f"Error in {script.name}: {e}", exc_info=True)
        sys.exit(1)

logger.info("Pipeline executed successfully!")
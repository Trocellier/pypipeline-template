# main.py -------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Sequential execution of pipeline scripts with error handling.

import runpy # runpy is used to run Python scripts dynamically
import sys   # sys is used for system-specific parameters and functions
from settings import logger, pipeline_scripts

logger.info("Starting pipeline execution...")

# Sequentially execute each script in the pipeline
for script in pipeline_scripts:
    logger.info(f"Running script: {script.name}")
    try:
        runpy.run_path(str(script), run_name="__main__")
    except Exception as e:
        logger.error(f"Error in {script.name}: {e}", exc_info=True)
        sys.exit(1)

logger.info("Pipeline executed successfully!")
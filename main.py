# main.py ------------------------------------------------------------------ #
# Author: Louis Trocellier
# Description: Production pipeline orchestrator.

from loguru import logger
import sys
import traceback
from importlib import util
from global import pipeline_scripts, SCRIPTS_DIR

# Main Execution Pipeline -------------------------------------------------- #
def main():
    """Execute the production pipeline."""
    logger.info("\n")
    logger.warning("=== Production Pipeline Started ===")
    
    try:
        for script_path in pipeline_scripts:
            script_name = script_path.stem
            logger.info(f"Running step: {script_name}")
            
            # Import and execute the script
            try:
                spec = util.spec_from_file_location(script_name, script_path)
                if spec and spec.loader:
                    module = util.module_from_spec(spec)
                    sys.modules[script_name] = module
                    spec.loader.exec_module(module)
                    
                    logger.info(f"Completed step: {script_name}")
            except Exception as e:
                logger.error(f"Failed to execute {script_name}: {e}")
                traceback.print_exc()
                raise
        
        logger.warning("=== Production Pipeline Completed Successfully ===")
        
    except Exception as e:
        logger.error(f"Pipeline failed during execution: {str(e)}")
        logger.error(traceback.format_exc())
        sys.exit(1)


# Launch ------------------------------------------------------------------- #
if __name__ == "__main__":
    main()

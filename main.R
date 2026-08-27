# main.R -------------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Production pipeline orchestrator.

# Initialization ------------------------------------------------------------ #
source("global.R")

# Main Execution Pipeline --------------------------------------------------- #
main <- function() {
  # Add a newline for better log readability
  log_info("\n")

  # Log the start of the production pipeline
  log_warn("=== Production Pipeline Started ===")
  
  tryCatch({
    for (script in pipeline_scripts) {
      script_name <- basename(script)
      log_info("Running step: {script_name}")
      
      source(script, local = FALSE)
      
      log_info("Completed step: {script_name}")
    }
    
    # Log the successful completion of the production pipeline
    log_warn("=== Production Pipeline Completed Successfully ===")
    
  }, error = function(e) {
    # Log the error and stop execution
    log_error("Pipeline failed during execution: {e$message}")
    stop(e)
  })
}

# Launch -------------------------------------------------------------------- #
if (!interactive()) {
  main()
} else {
  main()
}
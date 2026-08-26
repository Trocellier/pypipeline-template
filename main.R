# main.R -------------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Production pipeline orchestrator.

# Initialization ------------------------------------------------------------ #
source("global.R")

# Main Execution Pipeline --------------------------------------------------- #
main <- function() {
  log_info("=== Production Pipeline Started ===")
  
  tryCatch({
    for (script in pipeline_scripts) {
      script_name <- basename(script)
      log_info("Running step: {script_name}")
      
      source(script, local = FALSE)
      
      log_info("Completed step: {script_name}")
    }
    
    log_info("=== Production Pipeline Completed Successfully ===")
    
  }, error = function(e) {
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
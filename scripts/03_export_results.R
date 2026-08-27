# 03_export_results.R ------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 03 - Exporting final results.

# Execution ----------------------------------------------------------------- #
log_info("Starting step 03: Export results")

# 1. Load parameters/settings
settings <- export_results_settings()

# 2. Prepare final exports and reports
results <- export_results_execution(settings)

# 3. Write final outputs
export_results_exports(results)

log_info("Step 03 completed successfully")
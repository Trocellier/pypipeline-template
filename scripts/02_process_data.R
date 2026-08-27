# 02_process_data.R --------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 02 - Processing data.

# Execution ----------------------------------------------------------------- #
log_info("Starting step 02: Process data")

# 1. Load parameters/settings
settings <- process_data_settings()

# 2. Process data
processed_data <- process_data_execution(settings)

# 3. Export processed data to intermediate storage
process_data_exports(processed_data)

log_info("Step 02 completed successfully")
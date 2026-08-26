# 01_fetch_data.R ----------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Script for step 01 - Fetching data.

# Source associated functions ----------------------------------------------- #
source(file.path(cfg$paths$functions, "01_fetch_data.R"), local = TRUE)

# Execution ----------------------------------------------------------------- #
log_info("Starting step 01: Fetch data")

# 1. Load parameters/settings
settings <- fetch_data_settings()

# 2. Retrieve data
raw_data <- fetch_data_execution(settings)

# 3. Export raw data to intermediate storage
fetch_data_exports(raw_data)

log_info("Step 01 completed successfully")
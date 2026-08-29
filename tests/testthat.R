# testthat.R --------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Entry point for running the testthat suite.

library(testthat)

# Load global environment (packages, configs, helper functions)
source("global.R", chdir = TRUE)

# Save original logging configuration
orig_threshold <- logger::log_threshold()
orig_appender  <- logger::log_appender()

# Mute file logging and reduce output for tests
logger::log_threshold(logger::WARN)
logger::log_appender(logger::appender_stdout)

# Execute all test scripts inside tests/testthat/
test_dir("tests/testthat", reporter = "progress")

# Restore original logging configuration
logger::log_threshold(orig_threshold)
logger::log_appender(orig_appender)

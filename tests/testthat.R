# testthat.R --------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Entry point for running the testthat suite.

library(testthat)

# Load global environment (packages, configs, helper functions)
source("global.R", chdir = TRUE)

# Execute all test scripts inside tests/testthat/
test_dir("tests/testthat", reporter = "summary")
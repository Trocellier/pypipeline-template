# tests/testthat/helper.R ---------------------------------------------------- #
# Author: Louis Trocellier
# Description: Helper setup executed before running test cases.

# Silence logging outputs during tests
if (exists("log_threshold")) {
  logger::log_threshold(logger::FATAL)
}
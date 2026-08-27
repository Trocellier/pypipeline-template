# tests/testthat/test_example.R --------------------------------------------- #
# Author: Louis Trocellier
# Description: Example test suite verifying basic environment initialization.

# test that the configuration environment is correctly initialized 
test_that("Environment is correctly initialized", {
  expect_true(exists("cfg"))
  expect_true(is.list(cfg))
})
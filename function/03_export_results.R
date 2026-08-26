# 03_export_results.R ------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Helper functions for results export step.

#' Define parameters for exporting results
export_results_settings <- function() {
  list(
    input_file = file.path(cfg$paths$data, "processed_data.rds"),
    output_csv = file.path(cfg$paths$outputs, "final_summary.csv")
  )
}

#' Prepare final datasets or summary statistics
export_results_execution <- function(settings) {
  log_info("Reading processed data from: {settings$input_file}")
  processed_data <- readRDS(settings$input_file)
  
  log_info("Generating summary metrics")
  summary_df <- processed_data %>%
    dplyr::group_by(status) %>%
    dplyr::summarise(
      count = dplyr::n(),
      mean_value = mean(value, na.rm = TRUE),
      .groups = "drop"
    )
  
  return(list(full_data = processed_data, summary = summary_df))
}

#' Save final files to outputs folder
export_results_exports <- function(results) {
  output_path <- file.path(cfg$paths$outputs, "final_summary.csv")
  
  readr::write_csv(results$summary, file = output_path)
  log_info("Final summary CSV written to: {output_path}")
}
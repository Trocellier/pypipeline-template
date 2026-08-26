# global.R ------------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Load packages, project configuration, logging, and helper functions.

# Packages ------------------------------------------------------------------- #
library(config)
library(logger)
library(dplyr)
library(purrr)

# Configuration ------------------------------------------------------------- #
cfg <- config::get()
env_app <- environment()

# Logging Setup ------------------------------------------------------------- #
# Set log threshold dynamically based on configuration (INFO, WARN, etc.)
log_threshold(get(cfg$logging$level, envir = asNamespace("logger")))

# Configure file logging if enabled
if (isTRUE(cfg$logging$log_to_file)) {
  log_dir <- cfg$paths$logs %||% "logs"
  if (!dir.exists(log_dir)) dir.create(log_dir, recursive = TRUE)
  
  # appender_tee logs to both console and file simultaneously
  log_appender(appender_tee(file.path(log_dir, "pipeline.log")))
}

# Sourcing Functions -------------------------------------------------------- #
source_dossier <- function(chemin, envir = env_app, pattern = "\\.[Rr]$") {
  fichiers <- list.files(chemin, pattern = pattern, full.names = TRUE)
  invisible(lapply(fichiers, function(fichier) {
    sys.source(fichier, envir = envir, keep.source = TRUE)
  }))
}

source_dossier(cfg$paths$functions)

# Script Discovery ---------------------------------------------------------- #
get_pipeline_scripts <- function() {
  scripts <- list.files(
    cfg$paths$scripts, 
    pattern = "^[0-9]+.*\\.[Rr]$", 
    full.names = TRUE
  )
  scripts[order(as.integer(sub("^([0-9]+).*", "\\1", basename(scripts))))]
}

pipeline_scripts <- get_pipeline_scripts()
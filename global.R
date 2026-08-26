# global.R ------------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Packages, config, functions, and script discovery.

# Packages ------------------------------------------------------------------- #
library(config)
library(logger)
library(dplyr)
library(purrr)

# Configuration ------------------------------------------------------------- #
cfg <- config::get()
env_app <- environment()

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
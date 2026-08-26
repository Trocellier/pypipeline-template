# global.R ------------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Packages, config, and function sourcing.

# Packages ------------------------------------------------------------------- #
library(shiny)
library(shinydashboard)
library(dplyr)
library(ggplot2)
library(DT)

# Configuration ------------------------------------------------------------- #
cfg <- config::get()
env_app <- environment()

# Sourcing ------------------------------------------------------------------- #
source_dossier <- function(chemin, envir = env_app, pattern = "\\.[Rr]$") {
  fichiers <- list.files(chemin, pattern = pattern, full.names = TRUE)
  invisible(lapply(fichiers, function(fichier) {
    sys.source(fichier, envir = envir, keep.source = TRUE)
  }))
}

source_dossier(cfg$paths$functions)

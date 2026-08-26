# Functions — Common -------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Shared functions used across all tabs.

# Utilities ------------------------------------------------------------------ #
# TODO: Add common utility functions
common_utils <- function() {
  NULL
}

# Formatting ----------------------------------------------------------------- #
# TODO: Add common formatting functions
common_format <- function() {
  NULL
}

# Display -------------------------------------------------------------------- #
# Create a box with default styling
common_main_box <- function(x, title, status = "primary", solidHeader = TRUE, 
                       collapsible = TRUE, width = 12) {
  box(
    title = title,
    status = status,
    solidHeader = solidHeader,
    collapsible = collapsible,
    width = width,
    x
  )
}

# TODO: Add other common display functions
common_display <- function() {
  NULL
}

# Execution helper ---------------------------------------------------------- #
# Execute a reactive or function inside tryCatch and return NULL on error.
# `expr_fn` should be a function (a reactive is a function). If `notify` is
# TRUE and shiny is available, a notification will be shown on error.
safe_exec <- function(expr_fn, name = NULL, notify = FALSE) {
  if (is.null(name)) name <- deparse(substitute(expr_fn))
  tryCatch(
    expr_fn(),
    error = function(e) {
      msg <- paste0("Error in ", name, ": ", conditionMessage(e))
      message(msg)
      if (isTRUE(notify) && requireNamespace("shiny", quietly = TRUE)) {
        shiny::showNotification(msg, type = "error")
      }
      NULL
    }
  )
}

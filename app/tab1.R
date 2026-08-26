# Tab 1 --------------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Placeholder for tab 1.

tab1_title <- "Tab 1"
tab1_icon <- "square"

# UI Interface -------------------------------------------------------------- #
tab1_ui <- tagList(
  common_main_box(uiOutput("tab1_settings"), title = "Settings", status = "primary"),
  common_main_box(uiOutput("tab1_visualization"), title = "Visualization", status = "info"),
  common_main_box(uiOutput("tab1_exports"), title = "Exports", status = "warning")
)

# Server -------------------------------------------------------------------- #
tab1_server <- function(input, output, session) {
  ## Box 1: Settings
  settings_r <- reactive({ tab1_settings() })
  output$tab1_settings <- renderUI({
    settings_val <- safe_exec(settings_r, "tab1_settings")
    NULL
  })

  ## Box 2: Visualization
  visualization_r <- reactive({ tab1_visualization() })
  output$tab1_visualization <- renderUI({
    visualization_val <- safe_exec(visualization_r, "tab1_visualization")
    NULL
  })

  ## Box 3: Exports
  exports_r <- reactive({ tab1_exports() })
  output$tab1_exports <- renderUI({
    exports_val <- safe_exec(exports_r, "tab1_exports")
    NULL
  })
}

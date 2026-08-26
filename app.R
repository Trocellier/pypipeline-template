# app.R --------------------------------------------------------------------- #
# Author: Louis Trocellier
# Description: Shiny dashboard.

# Initialization ------------------------------------------------------------ #
source("global.R", local = TRUE)

tabs <- list.files(cfg$paths$app, pattern = "^tab[0-9]+.*\\.[Rr]$", full.names = TRUE)
tabs <- tabs[order(as.integer(sub("^tab([0-9]+).*", "\\1", basename(tabs))))]
invisible(lapply(tabs, sys.source, envir = env_app, keep.source = TRUE))

# UI Interface -------------------------------------------------------------- #
ui <- tagList(
  dashboardPage(
    skin = cfg$app$skin,
    dashboardHeader(
      title = cfg$app$title,
      titleWidth = 230
    ),
    dashboardSidebar(
      sidebarMenu(
        menuItem(tab1_title, tabName = "tab1", icon = icon(tab1_icon))
      )
    ),
    dashboardBody(
      tags$head(tags$link(rel = "stylesheet", type = "text/css", href = "custom.css")),
      tabItems(
        tabItem("tab1", tab1_ui)
      )
    )
  ),
  tags$footer(
    class = "app-footer",
    tags$div(
      class = "footer-left",
      tags$img(src = "logo.png", alt = cfg$app$author, class = "app-footer-logo"),
      tags$span(cfg$app$copyright, class = "copyright")
    ),
    tags$div(
      class = "footer-right",
      tags$span(paste0("v", cfg$app$version), class = "version")
    )
  )
)

# Server -------------------------------------------------------------------- #
server <- function(input, output, session) {
  tab1_server(input, output, session)
}

# Launch -------------------------------------------------------------------- #
shinyApp(ui, server)

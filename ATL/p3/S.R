# Install the shiny package if it's not already installed
# install.packages("shiny")

# Load the shiny package
library(shiny)

# Define UI
ui <- fluidPage(
  titlePanel("Simple Shiny Web Application"),
  sidebarLayout(
    sidebarPanel(
      textInput("name", "Enter your name:", ""),
      actionButton("submit", "Submit")
    ),
    mainPanel(
      textOutput("greeting")
    )
  )
)

# Define server logic
server <- function(input, output, session) {
  observeEvent(input$submit, {
    output$greeting <- renderText({
      paste("Hello, ", input$name, "!", sep = "")
    })
  })
}

# Run the application
shinyApp(ui = ui, server = server)

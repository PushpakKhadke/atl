# Install the shiny package if it's not already installed
# install.packages("shiny")


# Load the shiny package
library(shiny)

# Define UI (User Interface)
ui <- fluidPage(
  titlePanel("Simple Calculator"),
  
  # Input fields for the two numbers
  sidebarLayout(
    sidebarPanel(
      numericInput("num1", "Enter first number:", 0),
      numericInput("num2", "Enter second number:", 0),
      
      # Action buttons for the operations
      actionButton("add", "Add"),
      actionButton("subtract", "Subtract"),
      actionButton("multiply", "Multiply"),
      actionButton("divide", "Divide"),
    ),
    
    # Output to display result
    mainPanel(
      h3("Result:"),
      textOutput("result")
    )
  )
)

# Define server logic
server <- function(input, output, session) {
  
  # A reactive value to store the result
  result <- reactiveVal(0)
  
  # Observe when the Add button is clicked
  observeEvent(input$add, {
    result(input$num1 + input$num2)
  })
  
  # Observe when the Subtract button is clicked
  observeEvent(input$subtract, {
    result(input$num1 - input$num2)
  })
  
  # Observe when the Multiply button is clicked
  observeEvent(input$multiply, {
    result(input$num1 * input$num2)
  })
  
  # Observe when the Divide button is clicked
  observeEvent(input$divide, {
    if(input$num2 != 0) {
      result(input$num1 / input$num2)
    } else {
      result("Cannot divide by zero!")
    }
  })
  
  # Output the result to the UI
  output$result <- renderText({
    result()
  })
}

# Run the application
shinyApp(ui = ui, server = server)

# Install and load required packages
if (!require(rpart)) install.packages("rpart")
if (!require(rpart.plot)) install.packages("rpart.plot")
if (!require(party)) install.packages("party")

library(rpart)
library(rpart.plot)
library(party)

# Load a sample dataset for demonstration
# Here, we use the built-in 'readingSkills' dataset in the party package
data("readingSkills", package = "party")

# Select data for the decision tree
input.dat <- readingSkills[1:105, ]

# Create the tree
output.tree <- ctree(
  nativeSpeaker ~ age + shoeSize + score,
  data = input.dat
)

# Plot the tree
plot(output.tree)

# Optionally, save the plot as a file
# jpeg("decision_tree.jpeg")
# plot(output.tree)
# dev.off() # Close the file device
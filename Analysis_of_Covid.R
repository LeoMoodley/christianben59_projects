# Load necessary packages
library(tidyverse)
library(lubridate)
library(psych)
library(corrplot)
library(MASS)

# Load and clean data
data <- read_csv("large_data.csv") %>%
  filter(!is.na(date)) %>%
  mutate(date = ymd(date),
         age_group = if_else(age < 20, "Under 20", 
                             if_else(age >= 20 & age < 40, "20-39", 
                                     if_else(age >= 40 & age < 60, "40-59", "60+"))))

# Perform statistical analyses
# Calculate descriptive statistics
summary_stats <- data %>%
  select_if(is.numeric) %>%
  describe() 

# Calculate correlation matrix and visualize it
cor_matrix <- data %>%
  select_if(is.numeric) %>%
  cor(method = "pearson")
corrplot(cor_matrix, method = "number")

# Perform principal component analysis and visualize it
pca <- data %>%
  select_if(is.numeric) %>%
  prcomp(center = TRUE, scale. = TRUE)
biplot(pca, cex = 0.8)

# Perform logistic regression and visualize it
logistic_model <- glm(status ~ age + gender + race, data = data, family = binomial)
summary(logistic_model)
ggplot(data, aes(x = age, y = status, color = gender)) +
  geom_point() +
  geom_smooth(method = "glm", method.args = list(family = "binomial"), se = FALSE) +
  facet_grid(rows = vars(race), scales = "free_y") +
  labs(title = "Logistic Regression of COVID-19 Status by Demographic Factors",
       x = "Age",
       y = "Status",
       color = "Gender")

# Perform k-means clustering and visualize it
kmeans_model <- data %>%
  select_if(is.numeric) %>%
  scale() %>%
  kmeans(centers = 5)
data %>%
  mutate(cluster = kmeans_model$cluster) %>%
  ggplot(aes(x = age, y = cases, color = factor(cluster))) +
  geom_point() +
  labs(title = "K-Means Clustering of COVID-19 Data",
       x = "Age",
       y = "Cases",
       color = "Cluster")

# Export results
write_csv(summary_stats, "summary_stats.csv")
write_csv(cor_matrix, "cor_matrix.csv")
write_csv(as.data.frame(pca$x), "pca_results.csv")
write_csv(as.data.frame(logistic_model$coefficients), "logistic_results.csv")
write_csv(as.data.frame(kmeans_model$cluster), "kmeans_results.csv")

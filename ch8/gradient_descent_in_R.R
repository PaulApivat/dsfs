# source: https://towardsdatascience.com/machine-learning-fundamentals-via-linear-regression-41a5d11f5220
# Author: Conor McDonald

library(dplyr)
library(ggplot2)


n <- 200
bias <- 4
slope <- 3.5
dot <- `%*%`

x <- rnorm(n) * 2
x_b <- cbind(x, rep(1, n))
y <- bias + slope * x + rnorm(n)
df <- data_frame(x = x, y = y)

learning_rate <- 0.05
n_iterations <- 100
theta <- matrix(c(20,20))

b0 <- vector("numeric", length = n_iterations)
b1 <- vector("numeric", length = n_iterations)
sse_i <- vector("numeric", length = n_iterations)

ggplot(df, aes(x, y)) + 
    geom_point(alpha = 0.5) +
    theme_minimal()

# learning loop
for (iteration in seq_len(n_iterations)) { 
    yhat               <- dot(x_b, theta)          # predict using weights in theta
    residuals_b        <- yhat - y                 # calculate the residuals
    gradients          <- 2/n * dot(t(x_b), residuals_b) # calculate the gradients of MSE w.r.t model weights 
    theta              <- theta - learning_rate * gradients # update theta 
    
    sse_i[[iteration]] <- sum((y - dot(x_b, theta))**2)
    b0[[iteration]]    <- theta[2]
    b1[[iteration]]    <- theta[1]
    
}

model_i <- data.frame(model_iter = 1:n_iterations, 
                      sse = sse_i, 
                      b0 = b0, 
                      b1 = b1)

# plot learning loops
p1 <- df %>% 
    ggplot(aes(x=x, y=y)) + 
    geom_abline(aes(intercept = b0, 
                    slope = b1, 
                    colour = -sse, 
                    frame = model_iter), 
                data = model_i, 
                alpha = .50 
    ) +
    geom_point(alpha = 0.4) + 
    geom_abline(aes(intercept = b0, 
                    slope = b1), 
                data = model_i[100, ], 
                alpha = 0.5, 
                size = 2, 
                colour = "dodger blue") +
    geom_abline(aes(intercept = b0, 
                    slope = b1),
                data = model_i[1, ],
                colour = "red", 
                alpha = 0.5,
                size = 2) + 
    scale_color_continuous(low = "red", high = "grey") +
    guides(colour = FALSE) +
    theme_minimal()

p2 <- model_i[1:30,] %>%
    ggplot(aes(model_iter, sse, colour = -sse)) + 
    geom_point(alpha = 0.4) +
    theme_minimal() +
    labs(x = "Model iteration", 
         y = "Sum of Sqaured errors") + 
    scale_color_continuous(low = "red", high = "dodger blue") +
    guides(colour = FALSE)

# plot gradient descent
p1

# plot decrease in sse across iterations
p2

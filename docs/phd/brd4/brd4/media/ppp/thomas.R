library(spatstat)

intensity_levels <- c(1e-05, 1e-04, 5e-06)
sigma_levels <- c(0.0, 50.0)
kappa <- 5e-06
window_size <- owin(c(0, 10000), c(0, 10000))
r_range <- seq(0, 500.0, length.out = 200)

plot_point_pattern_and_L_function <- function(ppp, intensity, sigma) {
  par(mfrow = c(1, 2), mar = c(4, 4, 4, 1), oma = c(0, 0, 2, 0), cex = 1.0)
  plot(ppp, main="", cex = 0.2, cols = "black", pch = 16, las = 1)
  
  L <- Lest(ppp, r=r_range, correction = "none")
  L_scaled <- L$un - L$r
  env <- envelope(ppp, Lest, nsim = 39, rank = 1, r = r_range)
  
  env_hi_scaled <- env$hi - env$r
  env_lo_scaled <- env$lo - env$r
  plot(L$r, L_scaled, type = "l", xlab = "r (nm)", ylab = "L(r) - r", main = bquote(lambda == .(intensity) ~ ", " ~ sigma == .(sigma)), ylim = c(-50, 150), col = "blue")
  polygon(c(env$r, rev(env$r)), c(env_hi_scaled, rev(env_lo_scaled)), col = rgb(1, 0, 0, 0.2), border = NA)
  lines(env$r, L_scaled, col = "black")
}

plot_index <- 1
for (intensity in intensity_levels) {
  for (sigma in sigma_levels) {
    if (sigma == 0) {
      ppp <- rpoispp(intensity, win = window_size)
    } else {
      ppp <- rThomas(kappa, sigma, intensity / kappa, win = window_size)
    }
    
    plot_point_pattern_and_L_function(ppp, intensity, sigma)
    
    plot_index <- plot_index + 1
  }
}

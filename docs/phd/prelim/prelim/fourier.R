library(ggplot2)

df1 <- read.csv('230726_Hela_J549_1pM_1hr_j646_10pM_overnight_5mW_20mW-R-4-kde10p-frc.csv')
df2 <- read.csv('230726_Hela_J549_1pM_1hr_j646_10pM_overnight_5mW_20mW-R-4-kde20p-frc.csv')
df3 <- read.csv('230726_Hela_J549_1pM_1hr_j646_10pM_overnight_5mW_20mW-R-4-kde50p-frc.csv')

ggplot() +
  geom_line(data = df1, aes(x = Spatial_Frequency, y = FRC, color = "10%"), size = 1.2) +
  geom_line(data = df2, aes(x = Spatial_Frequency, y = FRC, color = "20%"), size = 1.2) +
  geom_line(data = df3, aes(x = Spatial_Frequency, y = FRC, color = "50%"), size = 1.2) +
  labs(x = expression('Spatial Frequency (nm'^-1*')'), y = 'Fourier Ring Correlation') +
  geom_hline(yintercept = 0.143, color = 'gray') +
  theme_minimal() +
  theme(legend.position = 'top',   
        panel.grid = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.line = element_line(color = 'black'),
        axis.text = element_text(size = 10)
  ) +
  coord_cartesian(xlim = c(0, 0.3)) +
  scale_color_manual(values = c("10%" = "#4169E1", "20%" = "red", "50%" = "black")) +
  guides(color = guide_legend(title = NULL))

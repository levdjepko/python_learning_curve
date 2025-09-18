import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(0, 20, 105)
plot.plot(x, np.sin(x))
# show a sine graph over a range
plot.show()


import matplotlib.pyplot as plt
import numpy as np

class Foo():
  
  def __init__(self):
    pass
  
  def graph(self):
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    plt.plot(xpoints, ypoints)
    plt.show()

test = Foo()
test.graph()

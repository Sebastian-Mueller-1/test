import matplotlib.pyplot as plt
import numpy as np
print("test")
class Foo():
  
  def __init__(self):
    pass
  
  def graph(self):
    x = np.linspace(0, 10, 100)
    fig, ax = plt.subplots(2)

    # Call plot() method on the appropriate object
    ax[0].plot(x, np.sin(x))
    ax[1].plot(x, np.cos(x))
    return fig
    

    
test = Foo()
figg = test.graph()
figg

print("hello")

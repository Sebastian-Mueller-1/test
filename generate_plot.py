from matplotlib import pyplot as plt
import numpy as np
import io

from flask import Flask, Response, send_file

app = Flask(__name__)

@app.route('/generate_plot')
def generate_plot():
    # Generate data for the plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # Create the plot
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Save the plot to a PNG file
    output = io.BytesIO()
    plt.savefig(output, format='png')
    output.seek(0)
    
    # Return the PNG file as a response
    return send_file(output, mimetype='image/png')

if __name__ == '__main__':
    app.run()

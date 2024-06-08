from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates"
)

def create_graph():
    filename = 'demo'

    # random but consistant data
    lst = [2,9,4,6,4]

    _min = min(lst)
    _max = max(lst)

    # Prepare arrays x, y, z
    theta = np.linspace(-(_min) * np.pi, _max * np.pi, 100)
    z = np.linspace(_min, _max, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)


    # clear buffer
    plt.clf()
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(x, y, z, label='parametric curve')
    plt.savefig(f'static/img/{filename}.png')

@app.route('/', methods=['GET'])
def getIndex():
    create_graph()
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
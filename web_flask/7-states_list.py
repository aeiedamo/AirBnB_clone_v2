#!/usr/bin/python3
"""
a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
        display a HTML page:
        H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted
    by name (A->Z)
    """
    states = sorted(list(storage.all("States").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exeception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

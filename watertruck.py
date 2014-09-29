# !/usr/bin/env python3

from random import sample
import os

from flask import Flask, jsonify

__version__ = "v1.0"

service = Flask(__name__)

# Sets a random value between 1 and 256 for the number of trucks to display
NUM_TRUCKS = range(2048)
# Eventually could globalize the value for ounces or Liters, this shows three 
# potential water bottle sizes: 12 oz, 20 oz, 24 oz
# AMOUNT_WATER = [12, 20, 24]

# Defines the API call for returning the number of trucks in JSON
@service.route("/{}/trucks".format(__version__), methods=["GET"])
def get_trucks():
    """Return jsonify'ed `trucks` value for a visualization."""
    # bottles = sample(AMOUNT_WATER, 1)
    # The response could eventually also have the size of bottles of water
    trucks = sample(NUM_TRUCKS, 1)
    resp = jsonify(trucks)
    resp.status_code = 200
    return resp


if __name__ == "__main__":
    service.run(debug=os.getenv("DEBUG", False))


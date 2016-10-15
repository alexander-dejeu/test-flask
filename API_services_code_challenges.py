""""0.  Instal Flask with pip install flask
        and test it with python -c "import flask"
    1.  Create a simple Flask web server that receives GET requests to the
        route `/hello` and responds with a friendly message. Test this route
        in your web browser and using Curl.
    2.  Add a new handler that receives POST requests to the route `/pets`
        with JSON data in the body and returns that JSON data unmodified in
        the response body. Test this route using Curl to ensure the `/pets`
        route responds correctly.
    3.  Modify the `/pets` handler to parse the JSON data, validate that
        it has the following fields: `name`, `age`, `species`. If it passes
        validation, store the parsed dictionary in a simple `pets` list.
        This will serve as a temporary database; `pets` will be saved in
        memory for the lifetime of the web server.
    4.  Add a new handler that receives GET requests to the route `/pets`
        and returns JSON data with a list of all pets.
    5.  Add a new handler that receives GET requests to the route
        `/pets/<name>` and checks if a pet with that name exists. If so,
        return a JSON representation of the pet. If not, return a HTTP 404
        error with a helpful JSON error message.
"""
from flask import Flask
from flask import request
import json


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home!'


@app.route('/hello')
def hello():
    return 'Hello World!'


@app.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == 'POST':
        result = request.form

        name = result['name']
        age = result['age']
        species = result['species']

        if name is not None and result is not None and species is not None:
            return 'proper data submited!'
        else:
            useful_message_for_user = 'Oops, looks like you are missing info'
            return 'find out which screwed up'
        return result["name"] + result["age"] + result["species"]
    else:
        return "petsss!"


if __name__ == "__main__":
    app.run()

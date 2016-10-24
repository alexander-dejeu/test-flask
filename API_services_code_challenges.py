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
    6.  Modify the `/pets` POST handler to not only validate that the JSON
        has the necessary fields (`name`, `age`, `species`), but also that
        `name` is unique among all pets. If valid, respond with a HTTP 201
        status code, otherwise 409 and a helpful error message in JSON. Test
        the `/pets` route to ensure it responds correctly to *both* valid
        and invalid POST requests.
    7.  Add a new handler that receives PUT requests to the route
        `/pets/<name>` and checks if a pet with that `name` exists. If not,
        respond with a HTTP 404 error and a helpful JSON error message. If so,
        validate the JSON data sent in the request body and update the pet
        with that `name` with all the new fields. If validation fails,
        respond with a HTTP 400 error.
    8.  Add a new handler that accepts DELETE requests to the route
        `/pets/<name>` and checks if a pet with that `name` exists. If so,
        delete the pet with that `name` and return a JSON representation of
        the deleted pet. If not, respond with a HTTP 404 error
        and a helpful JSON error message.
"""
from flask import Flask, request, json
from flask import jsonify

list_of_pets = []
app = Flask(__name__)


@app.route('/')
def home():
    return 'Home!'


@app.route('/hello')
def hello():
    return 'Hello World!'

"""Add a new handler that receives PUT requests to the route
    `/pets/<name>` and checks if a pet with that `name` exists. If not,
    respond with a HTTP 404 error and a helpful JSON error message. If so,
    validate the JSON data sent in the request body and update the pet
    with that `name` with all the new fields. If validation fails,
    respond with a HTTP 400 error."""
@app.route('/pets/<name>', methods=['GET', 'PUT'])
def getPet(name):
        if request.method == 'PUT':
            result = request.form

            for pet in list_of_pets:
                if pet['name'] == name:
                    # We found a pet with that name and can now update fields
                    if ((not(result['age'] == "")) & (not(result['species'] == ""))):
                        pet['age'] = result['age']
                        pet['species'] = result['species']
				        return 'it worked'
                    else:
                        return 'HTTP 400 Error: Bad Request -- Missing parameters.\n', 400

            return json.dumps({'error':'A pet with that name already exists'}), 404

        else:
            for pet in list_of_pets:
                if(pet['name'] == name):
                    return jsonify(pet)
        # abort(404)
            return '404 Error - page not found! :(', 404


@app.route('/pets', methods=['GET', 'POST'])
def pets():
    if request.method == 'POST':
        # Parse the request into a dictionary json object
        result = request.form
        print 'hello world!'
        print result

        name = result['name']
        age = result['age']
        species = result['species']

# QUESTION: In situations like this how do you break into smaller bits of code
        if ((not(name == "")) & (not(age == "")) & (not(species == ""))):
            # Check if the name is unique if so append to the list
            for pet in list_of_pets:
                if(pet['name'] == name):
                    # Issue where the name already exists
                    return json.dumps({'error':'name already exists'}), 409

            list_of_pets.append(result)
            return 'Pet was saved!', 201
        else:
            useful_message_for_user = 'Oops, looks like you are missing info!  Add: '
            if not('name' in result.keys()):
                useful_message_for_user += 'A name. '
            if not('age' in result.keys()):
                useful_message_for_user += 'An age. '
            if not('species' in result.keys()):
                useful_message_for_user += 'A species. '

            return useful_message_for_user

    # Get Request
    else:
        return json.dumps(list_of_pets)


if __name__ == "__main__":
    app.run()

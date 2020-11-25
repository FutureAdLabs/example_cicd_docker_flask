from flask import Flask, request, jsonify, make_response, send_file
from flask import Response, redirect, session, url_for
from flask import render_template, send_from_directory
from flask_restplus import reqparse
from flask_cors import CORS
from flask_basicauth import BasicAuth
import requests
import json
import lib.tools as tools
import sys

app = Flask(__name__, static_url_path='')

CORS(app)
# set this bugger by default.
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['Access-Control-Allow-Origin'] = '*'


@app.route('/js/<path:path>')
def send_js(path):
    # offer up the js and css files for consumption
    return send_from_directory('templates/js', path)


@app.route('/css/<path:path>')
def send_css(path):
    # offer up the js and css files for consumption
    return send_from_directory('templates/css', path)


@app.route('/images/<path:path>')
def send_image(path):
    # offer up the js and css files for consumption
    return send_from_directory('templates/images', path)


@app.route('/', methods=['POST', 'GET'])
def page_test():
    """ Sanity check for flask application (used in automated tests)

    """
    # get user-name and access rights from IAM

    html = "<h3>Hello world! 2</h3>"
    return html


@app.route('/demo', methods=['POST', 'GET'])
def demo_url():
    """ Sanity check for flask application (used in automated tests)

    """
    return render_template('demo_page.html')


def load_input():

    json_str = request.get_data()
    if json_str is None:
        json_str = request.get_json()
    else:
        print(json_str)
        try:
            json_str = json.loads(json_str)
        except:
            output = {"status": 401,
                      "message": "unable to process input data"}
            return json.dumps(output), 200, {'Content-Type': 'text/plain; charset=utf-8'}
    return json_str


@app.route('/api_call', methods=['POST', 'GET'])
def api_call():
    """Returns the nearest neighbors' indices and distances, as well
    as the objectives given by the user."""

    json_str = load_input()
    output = {
        'inputs': json_str,
        'results': 'cool results'}

    return json.dumps(output), 200, {'Content-Type': 'text/plain;charset=utf-8'}


def create_app():
    """ Constructor
    Returns
    -------
    app : flask app
    """
    return app

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 80
    app.run(debug=True, host='0.0.0.0', port=port)

from flask import Flask, jsonify, request, make_response
from todo.controllers import todo

app = Flask(__name__, static_url_path=None)

@app.route('/', methods=['GET', 'OPTIONS'])
def index():
    hasil = {'status_code': 200, 'description': 'Home Index'}
    return make_response(jsonify(hasil), 200)

app.register_blueprint(todo, url_prefix='/todo')
if __name__ == '__main__':
    app.run(debug=True)
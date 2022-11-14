from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)





@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/person")
def person_example():
    data_obj = {"name": "Josh", "id": 1}
    print(data_obj)
    return jsonify(person=data_obj)

if __name__ == '__main__':
    app.run(debug=True)

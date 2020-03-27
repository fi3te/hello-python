from flask import Flask, json

users = [{"id": 1, "name": "Max"}, {"id": 2, "name": "Jana"}]

app = Flask(__name__)
app.config['ENV'] = 'development'


@app.route('/user', methods=['GET'])
def get_users():
    return json.dumps(users)


if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, jsonify, request, json


def create_app():  # put application's code here
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='key'
    )

    @app.route('/good')
    def hello_world():
        return jsonify({'message': 'Hello, World!'})

    # job create, list
    @app.route('/job', methods=('GET', 'POST'))
    def job():
        if request.method == 'GET':
            with open("static/job.json", "r", encoding='utf-8') as f:
                jsondata = f.read()
                objs = json.loads(jsondata)

            return jsonify({'message': objs})
        if request.method == 'POST':
            with open("static/job.json", "r", encoding='utf-8') as f:
                jsondata = f.read()
                objs = json.dumps(json.loads(jsondata))

            with open("static/job.json", "a", encoding='utf-8') as f:
                f.write(objs)

            return jsonify({'message': "hello!!"})

    # job detail, update, delete
    @app.route('/job/<int:task_id>', methods=('GET', 'PUT', 'DELETE'))
    def job_detail():
        if request.method == 'GET':
            return 'Hello World!!'

    # job implement
    @app.route('/task', methods='POST')
    def task():
        if request.method == 'POST':
            return 'Hello World!!'

    return app

from flask import Flask, jsonify, json, request, render_template

from flaskr.utils import read, drop, write

import pandas as pd


def create_app():  # put application's code here
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False

    app.config.from_mapping(
        SECRET_KEY='key'
    )

    @app.route('/')
    def home():
        return jsonify({
            'api': 'api/task-running'
        })

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
    @app.route('/api/task-running', methods=('GET', 'POST'))
    def task():
        """
            작성자 : 강정희
            리뷰어 : 이형준
            변환을 원하는 csv 파일과 task 정보를 request 받아 task 수행 후 결과 반환
        """
        if request.method == 'GET':
            return render_template("index.html")

        if request.method == 'POST':
            request_csv = request.files['fileupload']
            job_id = int(request.form.get('job_id'))

            # request_csv 형식 예외처리
            if request_csv.content_type != 'text/csv':
                return jsonify({'error message': "CSV 파일을 업로드하세요."})

            # job_id와 맞는 task list check
            with open("flaskr/static/job.json", "r", encoding='utf-8') as f:
                jsondata = f.read()
                objs = json.loads(jsondata)

                for idx, value in enumerate(objs):
                    if value['jobid'] == job_id:
                        task_list = value['task_list']
                        read_path = value['property']['read']['filename']
                        column_name = value['property']['drop']['column_name']
                        write_path = value['property']['write']['filename']
                        break
                    else:
                        return jsonify({'error message': "지정한 작업이 없습니다."})

            # task_list 마지막 단계 확인 후 해당 단계 실행
            last_task = list(task_list.keys())[-1]

            if last_task == 'read':
                result = read(request_csv, read_path)
            elif last_task == 'drop':
                result = drop(request_csv, read_path, column_name)
                result_chk = type(result) == pd.core.frame.DataFrame
            elif last_task == 'write':
                result = write(request_csv, read_path, column_name, write_path)

            if last_task == 'read' or (last_task == 'drop' and result_chk):
                return result.to_html()
            else:
                return result

    return app


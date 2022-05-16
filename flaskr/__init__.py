import csv

from flask import Flask, jsonify, json, request, send_file

import pandas as pd

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

    # csv > DataFrame 리턴
    def _read(request_csv):
        print('read')
        # csv_dicts = [{k: v for k, v in row.items()}
        #              for row in csv.DictReader(request_csv.splitlines(), skipinitialspace=True)]
        if request_csv.content_type != 'text/csv':
            return jsonify({'error message': "CSV 파일을 업로드하세요"})
        return pd.read_csv(request_csv)

    # 지정된 컬럼을 제거한 DataFrame 리턴
    def _drop(request_csv, column_name):
        print('drop')
        df_csv = _read(request_csv)
        return df_csv.drop(columns=[column_name], inplace=True)

    # 지정된 파일 경로로 csv 파일 저장
    def _write(request_csv, column_name, write_path):
        print('write')
        df_csv = _drop(request_csv, column_name)
        save_file = df_csv.to_csv(write_path, encoding='utf-8')
        return send_file(save_file,
                         mimetypes='text/csv',
                         attachment_filename='download_csv.csv',
                         as_attachment=True
                         )

    # job implement
    @app.route('/task', methods=('GET', 'POST'))
    def task():
        """
            작성자 : 강정희
            변환을 원하는 csv 파일과 task 정보를 request 받아 task 수행 후 결과 반환
        """
        if request.method == 'POST':
            request_csv = request.files['fileupload'].read()
            job_id = request.form.get('job_id')
            # request_csv = ''
            # job_id = 1

            # job_id와 맞는 task list check
            with open("static/job.json", "r", encoding='utf-8') as f:
                jsondata = f.read()
                objs = json.loads(jsondata)

                for idx, value in enumerate(objs):
                    if value['jobid'] == job_id:
                        task_list = value['task_list']
                        column_name = value['property']['drop']['column_name']
                        write_path = value['property']['write']['filename']
                        break

            # task_list 마지막 단계 확인 후 해당 단계 실행
            last_task = list(task_list.keys())[-1]

            if last_task == 'read':
                result = _read(request_csv)
            elif last_task == 'drop':
                result = _drop(request_csv, column_name)
            elif last_task == 'write':
                result = _write(request_csv, column_name, write_path)

            if last_task == 'read' or last_task == 'drop':
                return result.to_html()
            else:
                return result

            # return 'Hello World!!'

    return app

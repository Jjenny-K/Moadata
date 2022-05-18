import uuid
import pandas as pd

from config import basedir
from flask import jsonify, request, json, Response


def form_data():
    """
        작성자 : 김채욱
        클라이언트가 입력한 새로운 job 정보를 호출
    """
    job = request.args.get('name')
    column = request.args.get('column')
    return job, column


def task_list(read, drop):
    """
        작성자 : 김채욱
        task_list 추가
    """
    if read and drop:
        task_list = {
            "read": ["drop"],
            "drop": ["write"],
            "write": []
        }
    elif read:
        task_list = {
            "read": ["drop"],
            "drop": []
        }
    else:
        task_list = {
            "read": []
        }

    return task_list


def post_data(job, column):
    """
        작성자 : 김채욱
        새로운 job 생성
    """
    new = {
        'jobid': uuid.uuid4(),
        'job_name': job,
        'task_list': {"read": ["drop"], "drop": ["write"], "write": []},
        'property': {
            "read": {"task_name": "read", "filename" : "path/to/a.csv", "sep": ","}, \
            "drop": {"task_name": "drop", "column_name": column}, \
            "write": {"task_name": "write", "filename" : "path/to/b.csv", "sep": ","}}
    }

    return new


def apply(data):
    """
        작성자 : 김채욱
        job.json file에 변경된 data를 적용한 후 변경된 data를 반환
    """
    with open('flaskr/data/job.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent="\t")
    return jsonify(data)


def bring_data():
    """
        작성자 : 김채욱
        job.json file에 전체 data 반환
    """
    with open('flaskr/data/job.json') as f:
        data = json.load(f)
    return data


def get_single_job(data, job_id):
    """
        작성자 : 강정희
        job.json file에서 job_id와 같은 값을 가진 job data 반환
    """
    job = None

    for ele in data:
        if ele['jobid'] == job_id:
            job = ele
            break

    return job


class TaskRunningProcessor:
    dataframe = None
    designated_path = '/flaskr/data/'

    def read(self, csv, job):
        """
            작성자 : 강정희
            지정된 파일 경로로 csv 형식 파일 저장 및 DataFrame 리턴
        """
        task = job['property']['read']

        # 입력된 csv 지정된 위치에 저장
        read_path = task['filename']
        filepath = basedir + self.designated_path + read_path
        csv.save(filepath)

        # csv to dataframe
        self.dataframe = pd.read_csv(filepath, delimiter=task['sep'])

        return self.dataframe

    def drop(self, job):
        """
            작성자 : 강정희
            지정된 컬럼을 제거한 DataFrame 리턴
        """
        task = job['property']['drop']

        # 삭제할 column_name 확인 및 처리
        column_name = task['column_name']
        if not (column_name in self.dataframe.columns):
            result = Response("{'error message': 'CSV 파일 내에 지정된 column이 없습니다.'}", status=400, mimetype='application/json')
        else:
            self.dataframe = self.dataframe.drop(columns=[column_name])
            result = self.dataframe

        return result

    def write(self, job):
        """
            작성자 : 강정희
            지정된 파일 경로로 csv 형식 파일 저장
            + 저장된 DataFrame 리턴
        """
        task = job['property']['write']

        # 지정된 위치에 csv 저장
        write_path = task['filename']
        filepath = basedir + self.designated_path + write_path
        self.dataframe.to_csv(filepath, sep=task['sep'], index=False, encoding='utf-8')
        return self.dataframe

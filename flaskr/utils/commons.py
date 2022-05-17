import csv
from config import basedir

from flask import jsonify, request, json
import pandas as pd

def task_list(read,drop):
    """
        task_list 추가
    """
    if read and drop:
        tasklist = {
            "read": [
                "drop"
            ],
            "drop": [
                "write"
            ],
            "write": []
        }
        return tasklist
    elif read:
        tasklist = {
            "read": [
                "drop"
            ],
            "drop": []
        }
        return tasklist
    else:
        tasklist = {
            "read": []
        }
        return tasklist

def apply(data):
    """
        json file에 변경된 data를 적용한 후 data를 반환
    """
    with open('job.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent="\t")
    return jsonify(data)



def form_data():
    """
        새로운 job 정보를 호출
    """
    job = request.args.get('name')
    column = request.args.get('column')
    return job, column



def post_data(job, column):
    """
        새로운 job 생성
    """
    new = {
    'jobid': uuid.uuid4(),
    'job_name': job,
    'task_list': {"read": ["drop"], "drop":["write"], "write":[]},
    'property': {"read": {"task_name": "read", "filename" : "path/to/a.csv", "sep" :","}, \
        "drop" : {"task_name": "drop", "column_name": column}, \
        "write" : {"task_name": "write", "filename" : "path/to/b.csv", "sep": ","}}
    }



def bring_data():
    """
        전체 data를
    """
    with open('job.json') as f:
        data = json.load(f)
    return data


def read(request_csv, read_path):
    """
        작성자 : 강정희
        csv > 지정된 위치 저장 및 DataFrame 리턴
    """
    # csv_dicts = [{k: v for k, v in row.items()}
    #              for row in csv.DictReader(request_csv.splitlines(), skipinitialspace=True)]
    filepath = basedir + read_path + request_csv.filename
    request_csv.save(filepath)

    return pd.read_csv(filepath)


def drop(request_csv, read_path, column_name):
    """
        작성자 : 강정희
        지정된 컬럼을 제거한 DataFrame 리턴
    """
    df_csv = read(request_csv, read_path)

    if not (column_name in df_csv.columns):
        return jsonify({'error message': "CSV 파일 내에 지정된 column이 없습니다"})

    return df_csv.drop(columns=[column_name])


def write(request_csv, read_path, column_name, write_path):
    """
        작성자 : 강정희
        지정된 파일 경로로 csv 형식 파일 저장
    """
    df_csv = drop(request_csv, read_path, column_name)
    filepath = basedir + write_path
    df_csv.to_csv(filepath, encoding='utf-8')

    return jsonify({'message': "Success"})

import csv
from config import basedir

from flask import jsonify
import pandas as pd


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

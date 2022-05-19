import json
import os
import sys

sys.path.append((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from config import basedir
from flask import Flask

from flaskr.views import HomeView, TaskRunView, JobView


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.from_mapping(
    SECRET_KEY='key'
)


"""
    API 명세
    GET /api/jobs: job.json 파일 내 job list 조회
    POST /api/jobs: 새로운 job 생성
    GET /api/job?job_id=<str:pk>: 입력된 job uuid 값과 같은 job 정보 상세 조회
    PATCH /api/job?job_id=<str:pk>: 입력된 job uuid 값과 같은 job 정보 수정
    DELETE /api/job?job_id=<str:pk>: 입력된 job uuid 값과 같은 job 정보 삭제
    POST /api/task-running: 입력한 csv 파일과 job_id 정보로 지정된 작업(job) 실행
"""


def make_json(self, file_path, data):
    """
        작성자 : 김채욱
        job.json 파일 생성
    """
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)


def make_file(self):
    """
        작성자 : 강정희
        지정된 경로에 폴더를 생성
    """
    # designated_path 경로로 지정된 폴더가 없을 경우 디렉토리 자동 생성
    designated_path = '/flaskr/data/'
    if not os.path.exists(os.path.join(basedir + designated_path)):
        os.mkdir(basedir + designated_path)

    # json_file_path 경로에 job.json 파일이 없을 경우 파일 자동 생성
    file_path = basedir + designated_path + 'job.json'
    data = []
    if not os.path.isfile(file_path):
        self.make_json(file_path, data)

home_view = HomeView.as_view('home_view', template_name='index.html')
task_view = TaskRunView.as_view('task_view')
job_view = JobView.as_view('job_view')

app.add_url_rule('/', view_func=home_view)
app.add_url_rule('/api/jobs', methods=['GET', 'POST'], view_func=job_view)
app.add_url_rule('/api/job', methods=['GET', 'PATCH', 'DELETE'], view_func=job_view)
app.add_url_rule('/api/task-running', view_func=task_view)

if __name__ == '__main__':
    app.run()
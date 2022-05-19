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


home_view = HomeView.as_view('home_view', template_name='create_job.html')
task_view = TaskRunView.as_view('task_view')
job_view = JobView.as_view('detailjob')


app.add_url_rule('/', view_func=home_view)
app.add_url_rule('/api/jobs', methods=['GET', 'POST'], view_func=job_view)
app.add_url_rule('/api/job', methods=['GET', 'PATCH', 'DELETE'], view_func=job_view)
app.add_url_rule('/api/task-running', view_func=task_view)


from flaskr.views import EditView, CsvView
edit_view = EditView.as_view('edit_view', template_name='modify_job.html')
csv_view = CsvView.as_view('csv_view', template_name='get_csv.html')
app.add_url_rule('/client/edit', methods=['GET'], view_func=edit_view)
app.add_url_rule('/client/csv', methods=['GET'], view_func=csv_view)

if __name__ == '__main__':
    app.run()

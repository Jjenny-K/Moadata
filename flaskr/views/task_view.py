import pandas as pd

from flask import request, Response
from flask.views import View
from flaskr.utils.commons import TaskRunningProcessor, CRUDTask

class TaskRunView(View, CRUDTask):
    """
        작성자 : 강정희
        리뷰어 : 이형준
        변환을 원하는 csv 파일과 task 정보를 request 받아 task 수행 후 결과 반환
    """
    template_name = None
    methods = ['GET', 'POST']
    result = None

    def __init__(self, template_name):
        self.template_name = template_name

    def run(self, job, task, task_processor, csv):
        if not task_processor:
            task_processor = TaskRunningProcessor()

        next_tasks = job['task_list'].get(task, [])

        if task.lower() == 'read':
            self.result = task_processor.read(csv, job)
        elif task.lower() == 'drop':
            self.result = task_processor.drop(job)
        elif task.lower() == 'write':
            self.result = task_processor.write(job)

        if task is not None and (type(self.result) == pd.core.frame.DataFrame):
            for task in next_tasks:
                self.run(job, task, task_processor, csv=None)

        return self.result

    def dispatch_request(self):
        if request.method == 'POST':
            request_csv = request.files['filename']
            job_id = int(request.form.get('job_id'))

            # request_csv 형식 예외처리
            if request_csv.content_type != 'text/csv':
                return Response("{'error message': 'CSV 파일을 업로드하세요.'}", status=400, mimetype='application/json')

            # job_id와 맞는 task list check
            try:
                data = self.get_all_jobs()
                job = self.get_single_job(data, job_id)
            except Exception as e:
                return Response("{'error message': '지정한 작업이 없습니다.'}", status=400, mimetype='application/json')

            # task_list 확인 후 해당 단계 실행
            # 모든 데이터의 흐름은 'read'로 시작한다고 가정
            first_task = 'read'

            result = self.run(job, first_task, task_processor=None, csv=request_csv)
            if type(result) == pd.core.frame.DataFrame:
                return Response(result.to_csv(index=False), status=201, mimetype='application/json')
            else:
                return result
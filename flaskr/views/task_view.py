from config import basedir
import pandas as pd

from flask import render_template, request, Response, json
from flask.views import View
from flaskr.utils import bring_data


class TaskRunningProcessor:
    dataframe = None

    def read(self, csv, job):
        """
            작성자 : 강정희
            csv > 지정된 위치 저장 및 DataFrame 리턴
        """
        task = job['property']['read']

        # 입력된 csv 지정된 위치에 저장
        read_path = task['filename']
        filepath = basedir + read_path + csv.filename
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
            return jsonify({'error message': "CSV 파일 내에 지정된 column이 없습니다"})
        self.dataframe = self.dataframe.drop(columns=[column_name])

        return self.dataframe

    def write(self, job):
        """
            작성자 : 강정희
            지정된 파일 경로로 csv 형식 파일 저장
        """
        task = job['property']['write']

        # 지정된 위치에 csv 저장
        write_path = task['filename']
        filepath = basedir + write_path
        self.dataframe.to_csv(filepath, sep=task['sep'], encoding='utf-8')

        return self.dataframe


class TaskRunView(View):
    template_name = None
    methods = ['GET', 'POST']

    def __init__(self, template_name):
        self.template_name = template_name

    def run(self, job, task, task_processor, csv):
        if not task_processor:
            task_processor = TaskRunningProcessor()

        next_tasks = job['task_list'].get(task, [])
        print(task, next_tasks)

        if task.lower() == 'read':
            task_processor.read(csv, job)
        elif task.lower() == 'drop':
            task_processor.drop(job)
        elif task.lower() == 'write':
            task_processor.write(job)

        if task:
            for task in next_tasks:
                self.run(job, task, task_processor, csv=None)


    def dispatch_request(self):
        # return render_template(self.template_name)
        if request.method == 'GET':
            return render_template(self.template_name)

        if request.method == 'POST':
            request_csv = request.files['fileupload']
            job_id = int(request.form.get('job_id'))

            # request_csv 형식 예외처리
            if request_csv.content_type != 'text/csv':
                # return jsonify({'error message': "CSV 파일을 업로드하세요."})
                # raise TypeError(f'CSV 파일을 업로드하세요.')
                # raise Exception(f'400 : CSV 파일을 업로드하세요.')
                return Response("{'error message': 'CSV 파일을 업로드하세요.'}", status=400, mimetype='application/json')

            # job_id와 맞는 task list check
            data = bring_data()
            for ele in data:
                if ele['jobid'] == job_id:
                    job = ele
                    break
            # print([ele for ele in data if int(ele['jobid']) == job_id])
            # job = [ele for ele in data if int(ele['jobid']) == job_id][0]
            if not job:
                return Response("{'error message': '지정한 작업이 없습니다.'}", status=400, mimetype='application/json')

            # task_list 확인 후 해당 단계 실행
            first_task = 'read'

            # if last_task == 'read' or (last_task == 'drop' and result_chk):
            #     return result.to_html()
            # else:
            #     return result

            print(self.run(job, first_task, task_processor=None, csv=request_csv))

            return self.run(job, first_task, task_processor=None, csv=request_csv)

from flask.views import MethodView
from flask import jsonify, request
from flaskr.utils.commons import CRUDTask


class JobView(MethodView, CRUDTask):
    """
        작성자 : 김채욱
        장고 View를 참고하여서 handler methods별로 나누어 실행
    """
    
    task = CRUDTask()
    data = task.get_all_jobs()
        

    def get(self):
        job_id = self.get_single_id()
        
        if job_id:
            return jsonify([ ele for ele in self.data if ele['job_id'] == job_id ][0]), 200
        else:
            return jsonify(self.data), 200

    def post(self):
        new_job = self.post_data()
        self.data.append(new_job)
        self.petch_data(self.data)
        return jsonify(self.data), 201

    def delete(self):
        job_id = self.get_single_id()
        print(job_id)
        self.data.pop([ i for i in range(len(self.data)) if self.data[i]['job_id'] == job_id  ][0])
        return self.petch_data(self.data), 204


    def patch(self):
        query = request.args.to_dict()
        job_id = query.get('job_id')
        job = query.get('name') 
        column = query.get('column')

        for ele in self.data:
            if ele["job_id"] == job_id:
                ele['job_name'] = job
                if ele['property']['drop']:
                    ele['property']['drop']["column_name"] = column
                    

        return self.petch_data(self.data), 200

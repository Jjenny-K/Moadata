from flask.views import MethodView
from flask import jsonify, request
from flaskr.utils import petch_data, form_data, post_data, get_all_jobs, get_single_id


class JobView(MethodView):
    data = get_all_jobs()

    def get(self):
        job_id = get_single_id()

        if job_id:
            return jsonify([ele for ele in self.data if ele['jobid'] == job_id][0]), 200
        else:
            return jsonify(self.data), 200

    def post(self):
        job, column, file, task = form_data()
        print(job, column, file, task)
        new_job = post_data(job, column, file, task)
        self.data.append(new_job)
        petch_data(self.data)
        return jsonify(self.data), 201

    def delete(self):
        job_id = get_single_id()

        self.data.pop([i for i in range(len(self.data)) if self.data[i]['jobid'] == job_id][0])
        return petch_data(self.data), 200

    def patch(self):
        job_id = get_single_id()

        query = request.args.to_dict()
        job = query.get('name')
        column = query.get('column')

        for ele in self.data:
            if ele['jobid'] == job_id:
                ele['job_name'] = job
                if ele['property']['drop']:
                    ele['property']['drop']["column_name"] = column

        return petch_data(self.data), 200
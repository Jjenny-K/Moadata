from flask import jsonify, request, json
import uuid


# helper function
def write(data):
    with open('job.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent="\t")
    return jsonify(data)


# helper function
def form_data():
    job = request.args.get('name')
    column = request.args.get('column')
    return job, column


# helper function
def post_data(job, column):
    new = {
    'jobid': uuid.uuid4(),
    'job_name': job,
    'task_list': {"read": ["drop"], "drop":["write"], "write":[]},
    'property': {"read": {"task_name": "read", "filename" : "path/to/a.csv", "sep" :","}, \
        "drop" : {"task_name": "drop", "column_name": column}, \
        "write" : {"task_name": "write", "filename" : "path/to/b.csv", "sep": ","}}
    }


# helper function
def bring_data():
    with open('job.json') as f:
        data = json.load(f)
    return data
from flask import Flask

from flaskr.views import HomeView, TaskRunView, JobView

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.from_mapping(
    SECRET_KEY='key'
)

home_view = HomeView.as_view('home_view', template_name='index.html')
task_view = TaskRunView.as_view('task_view', template_name='task_running.html')
job_view = JobView.as_view('detailjob')

app.add_url_rule('/', view_func=home_view)
app.add_url_rule('/api/task-running', view_func=task_view)
app.add_url_rule('/api/jobs', methods=['POST'], view_func=job_view)
app.add_url_rule('/api/jobs', methods=['GET'], defaults={'job_id':None} ,view_func=job_view)
app.add_url_rule('/api/job/<job_id>', methods=['GET','PATCH', 'DELETE'], view_func=job_view)



if __name__ == '__main__':
    app.run()

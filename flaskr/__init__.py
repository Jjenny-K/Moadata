from flask import Flask

from flaskr.views import HomeView, TaskRunView, JobView, EditView, CsvView

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config.from_mapping(
    SECRET_KEY='key'
)

home_view = HomeView.as_view('home_view', template_name='create_job.html')
task_view = TaskRunView.as_view('task_view', template_name='task_running.html')
job_view = JobView.as_view('detailjob')
edit_view = EditView.as_view('edit_view', template_name='create_job.html')
csv_view = CsvView.as_view('csv_view', template_name='get_csv.html')

app.add_url_rule('/', view_func=home_view)
app.add_url_rule('/api/task-running', view_func=task_view)
app.add_url_rule('/api/jobs', methods=['POST'], view_func=job_view)
app.add_url_rule('/api/jobs', methods=['GET'], view_func=job_view)
app.add_url_rule('/api/job', methods=['GET', 'PATCH', 'DELETE'], view_func=job_view)
app.add_url_rule('/client/edit', methods=['GET'], view_func=edit_view)
app.add_url_rule('/client/csv', methods=['GET'], view_func=csv_view)


if __name__ == '__main__':
    app.run()
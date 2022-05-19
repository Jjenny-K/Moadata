from flask import render_template, jsonify
from flask.views import View


class HomeView(View):
    template_name = None

    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        # return render_template(self.template_name)
        return jsonify({
            'apis': [
                'api/jobs',
                'api/jobs?job_id=<str:pk>',
                'api/task-running'
            ]
        })

from flask import render_template
from flask.views import View


class HomeView(View):
    template_name = None

    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)


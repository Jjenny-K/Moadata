from flask import Flask, render_template, request, redirect, url_for
from config import basedir
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/api/job', methods=['POST'])
def creat_job():
    if request.method == 'POST':
        result = request.form
        print(result)
        return render_template("index.html", result=result)


@app.route('/csv', methods=["POST"])
def csv_upload():
    if request.files['filename']:
        uploaded_file = request.files['filename']
        filepath = os.path.join(basedir, uploaded_file.filename)
        filename = uploaded_file.filename
        print(f'file: {(uploaded_file.content_type)}')
        print(f'file_path: {filepath}')
        print(f'file_name: {filename}')
        if uploaded_file.content_type != 'text/csv':
            return "CSV 파일을 업로드하세요"
        uploaded_file.save(filepath)
        return "SAVE SUCCESS"
    return "SAVE FAIL"

if __name__ == '__main__':
    app.run()

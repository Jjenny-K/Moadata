from flask import Flask, render_template, request, jsonify
from config import basedir
import os

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/jobs', methods=['GET', 'POST', 'DELETE'])
def job():
    if request.method == 'GET':
        return jsonify({"test": "test"})
    elif request.method == 'POST':
        result = request.form
        print(result)
        return render_template("index.html")
    elif request.method == 'DELETE':
        result = request.form
        print(result)
        return 'DELETE SUCCESS'

@app.route('/csv', methods=["POST"])
def csv_upload():
    if request.files['file']:
        uploaded_file = request.files['file']
        filepath = os.path.join(basedir, uploaded_file.filename)
        filename = uploaded_file.filename
        print(f'file: {(uploaded_file.content_type)}')
        print(f'file_path: {filepath}')
        print(f'file_name: {filename}')
        if uploaded_file.content_type != 'text/csv':
            return jsonify({"message": "csv 업로드하세요"})
        uploaded_file.save(filepath)
        return "SAVE SUCCESS"
    message = "업로드할 파일이 없습니다."
    return jsonify({"message": message})


@app.route('/jobs', methods=["PUT"])
def put_confirm():
    return "I'm PUT"


if __name__ == '__main__':
    app.run()

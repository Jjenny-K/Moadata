from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/csv', methods=["POST"])
def csv_upload():
    data = []
    if request.method == 'POST':
        if request.files:
            uploaded_file = request.files['filename']
            uploaded_file.save(os.path.join(app.config['FILE_UPLOADS'], uploaded_file.filename))
            f = request.form['filename'] # This is the line throwing the error
            with open(f) as file:
                csv_file = csv.reader(file)
                for row in csv_file:
                    data.append(row)
            return redirect(request.url)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()

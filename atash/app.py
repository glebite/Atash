"""app.py

"""
from flask import Flask
from flask import render_template, request
from werkzeug.utils import secure_filename


# instantiate the application
app = Flask(__name__)


@app.route('/')
def index():
    """index
    """
    return render_template('index.html', pageTitle='آتش')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    """upload_file
    """
    if request.method == 'POST':
        f = request.files['file-input']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'


if __name__ == "__main__":
    app.run(debug=True)

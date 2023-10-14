import os
from flask import Flask, render_template, request, send_file, redirect, session, url_for


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'



#Upload and Download


def get_uploaded_files():
    return os.listdir(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    files = get_uploaded_files()
    return render_template('index.html', files=files)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            return redirect('/')
    return render_template('upload_form.html')
        

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
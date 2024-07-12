from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash
import os
from collections import defaultdict

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'supersecretkey'

# 确保上传文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# 用于存储文件分类的字典
file_categories = defaultdict(list)

@app.route('/', methods=['GET'])
def index():
    categorized_files = defaultdict(list)
    for filename, category in file_categories.items():
        categorized_files[category].append(filename)
    return render_template('index.html', categorized_files=categorized_files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(url_for('index'))
    file = request.files['file']
    category = request.form['category']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('index'))
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_categories[filename] = category
        flash('File successfully uploaded')
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)

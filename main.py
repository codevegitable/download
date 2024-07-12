from flask import Flask, request, redirect, url_for, render_template, flash, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# 获取用户的主目录
home_dir = os.path.expanduser('~')
upload_folder = os.path.join(home_dir, 'uploads')
app.config['UPLOAD_FOLDER'] = upload_folder

# 创建上传文件夹
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# 主页
@app.route('/')
def index():
    categorized_files = {
        '补丁': [],
        'galgame': [],
        '本子': []
    }
    
    # 添加新的分类（可以在这里添加新的分类）
    # categorized_files['新的分类'] = []
    
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        category = filename.split('_')[0]
        if category in categorized_files:
            categorized_files[category].append(filename)
    
    return render_template('index.html', categorized_files=categorized_files)

# 文件上传
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    category = request.form['category']
    if file and category:
        filename = category + '_' + file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('文件上传成功')
    else:
        flash('请填写所有字段')
    return redirect(url_for('index'))

# 文件下载
@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

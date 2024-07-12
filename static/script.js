document.getElementById('fileInput').addEventListener('change', function(event) {
    var fileName = this.files[0].name;
    document.getElementById('currentFile').innerHTML = '当前文件: ' + fileName;
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var form = this;
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    var progressBar = document.getElementById('progressBar');
    var uploadSpeed = document.getElementById('uploadSpeed');
    var startTime = new Date().getTime();

    xhr.upload.addEventListener('progress', function(event) {
        if (event.lengthComputable) {
            var percentComplete = Math.round((event.loaded / event.total) * 100);
            progressBar.style.width = percentComplete + '%';
            progressBar.innerHTML = percentComplete + '%';
            progressBar.style.left = '50%'; /* 保持文字在进度条中央 */
        }

        var currentTime = new Date().getTime();
        var timeElapsed = (currentTime - startTime) / 1000; // 以秒计
        var uploadSpeedKBps = (event.loaded / 1024 / timeElapsed).toFixed(2);
        uploadSpeed.innerHTML = '网速: ' + uploadSpeedKBps + ' KB/s';
    });

    xhr.addEventListener('load', function(event) {
        // 上传完成后刷新页面显示新文件列表
        window.location.reload();
    });

    xhr.open('POST', form.action);
    xhr.send(formData);
});

function showCategory(category) {
    var fileLists = document.getElementsByClassName('file-list');
    for (var i = 0; i < fileLists.length; i++) {
        fileLists[i].classList.remove('active');
    }
    document.getElementById(category).classList.add('active');
}
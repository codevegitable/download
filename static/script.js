function showCategory(category) {
    var lists = document.querySelectorAll('.file-list');
    lists.forEach(function(list) {
        list.classList.remove('active');
    });
    document.getElementById(category).classList.add('active');
}

document.getElementById('fileInput').addEventListener('change', function(event) {
    var fileName = event.target.files[0].name;
    document.getElementById('currentFile').innerText = fileName;
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var form = this;
    var formData = new FormData(form);
    var xhr = new XMLHttpRequest();
    var progressBar = document.getElementById('progressBar');

    xhr.upload.addEventListener('progress', function(event) {
        if (event.lengthComputable) {
            var percentComplete = Math.round((event.loaded / event.total) * 100);
            progressBar.style.width = percentComplete + '%';
            progressBar.innerHTML = percentComplete + '%';
        }
    });

    xhr.addEventListener('load', function(event) {
        window.location.reload();
    });

    xhr.open('POST', form.action);
    xhr.send(formData);
});

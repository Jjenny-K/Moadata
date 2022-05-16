$("#subFile").change(function () {

    let data = new FormData();
    let files = $("subFile").get(0).files;
    if (files.length > 0) {
        data.append("csvFiles", files[0]);
    }
    $.ajax({
        url: "/csv",
        type: "POST",
        processData: false,
        contentType: false,
        data: data,
        success: function (response) {
            console.log('전송 성공')
        },
        error: function (er) {
            alert('전송 실패');
        }
    });
});

function isValid(event) {
    const sec = document.querySelector('#upload-section');
    const uploadBox = sec.querySelector('.upload-box');

    uploadBox.addEventListener('dragover', function (event) {
        event.preventDefault();
        let validator = event.dataTransfer.types.indexOf('Files');
        if (validator < 0) {
            alert('파일을 업로드하세요');
            return false;
        }
        if (event.dataTransfer.files[0].type !== "text/csv") {
            alert("csv 파일을 업로드하세요");
            return false;
        }
        if (event.dataTransfer.files.length > 1) {
            alert('파일은 하나씩 전송이 가능합니다.');
            return false;
        }
    })
};


const sec = document.querySelector('#upload-section');
const uploadBox = sec.querySelector('.upload-box');

uploadBox.addEventListener('dragover', function (e) {
    if (e.dataTransfer.types.indexOf('Files') < 0) {
        this.style.backgroundColor = 'red';
    } else {
        this.style.backgroundColor = '#3399FF';
    }
});


/* 박스 밖으로 나갈 때 */
uploadBox.addEventListener('dragleave', function (e) {
    this.style.backgroundColor = 'white';
});

/* 박스 안에서 Drag를 Drop했을 때 */
uploadBox.addEventListener('drop', function (e) {
    e.preventDefault();
    isValid(e);
    this.style.backgroundColor = 'white';
    console.dir(e.dataTransfer);
    console.dir(e.dataTransfer.files[0]);
});

$(document).ready(function () {
    let jobList = document.querySelector('.job-list');
    jobList.innerHTML = "";
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/jobs",
        success: function (response) {
            console.log(response);
            jobs = response;
            indent = '&nbsp;&nbsp;&nbsp;&nbsp;'
            for (let i = 0; jobs.length <= 30; i++) {
                // console.log(jobs[i]);
                let tempHtml = `<div>{<br>                                               
                            }<br>
                            </div>`
                jobList.innerHTML += tempHtml
                if (i === 50) break;
            }
        }
    })
});


function fixJob() {
    console.log("fixJob execute");
    let jobId = $('.job_id').val();
    let jobName = $('.job_name').val();
    let columnName = $('.column_name').val();
    console.log(jobId, jobName, columnName);
    if (jobId === "" || jobName === "" || columnName === "") {
        alert('값을 다 입력하세요');
        return;
    }
    $.ajax({
        type: "PUT",
        url: `http://127.0.0.1:5000/job?jogId=${jobId}&column=${columnName}&name=${jobName}`,
        success: function (response) {
            console.log(response);
            alert('조회 성공.');
        },
        error: function (data) {
            alert("수정 실패");
        }
    })
}

function getJob() {
    let jobId = $('.get-job-id').val();
    console.log(jobId);
    if (jobId === "") {
        alert('값을 입력하세요.');
        return;
    }
    $.ajax({
        type: "DELETE",
        url: `http://127.0.0.1:5000/jobs${jobId}`,
        success: function (response) {
            console.log(response);
            alert('조회 성공.');
        },
        error: function (data) {
            alert("조회 실패");
        }
    })
};


function postCSV() {
    let fileInput = $('#csvFile')[0];
    console.log("fileInput: ", fileInput.files);
    if (fileInput.files.length === 0) {
        alert("파일을 선택해주세요");
        return;
    }
    let formData = new FormData();
    formData.append("file", fileInput.files[0]);
    $.ajax({
        type: 'POST',
        url: "http://127.0.0.1:5000/csv",
        data: formData,
        contentType: false,
        processData: false,
        cache: false,
        success: function (data) {
            alert("성공");
            console.log(data.message);
        },
        error: function (data) {
            alert("실패");
            console.log(data.message);
        }
    })
};

function jobDelete() {
    let queryString = $('.del-job-id').val();
    if (queryString === "") {
        alert('값을 입력하세요.');
        return;
    }
    $.ajax({
        type: "DELETE",
        url: `http://127.0.0.1:5000/job?jobId=${jobId}`,
        success: function (response) {
            console.log(response);
            alert('삭제되었습니다.');
        }
    })
};

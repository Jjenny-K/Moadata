const localhost = "http://127.0.0.1:5000";


$(document).ready(function () {
    let jobList = document.querySelector('.job-list');
    // jobList.innerHTML = "";
    $.ajax({
        type: "GET",
        url: `${localhost}/jobs`,
        success: function (response) {
            console.log(response);
            jobs = response;
            indent = '&nbsp;&nbsp;&nbsp;&nbsp;'
            for (let i = 0; jobs.length; i++) {
                let tempHtml = `<div>{<br>                                             
                            }<br>
                            </div>`

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
        url: `${localhost}/job?jogID=${jobId}&column=${columnName}&name=${jobName}`,
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
    let jobIdSection = $('.christ')
    console.log(jobIdSection);
    console.log(jobId);
    if (jobId === "") {
        alert('값을 입력하세요.');
        return;
    }
    let jobID = `{"jobID": ${jobId}}`;
    $.ajax({
        type: "POST",
        url: `${localhost}/jobs/${jobId}`,
        data: JSON.stringify(jobID),
        contentType: 'application/json',
        success: function (response) {
            console.log(response);
            alert('조회 성공.');
            jobIdSection.empty()
            jobIdSection.append(`<div>${response}</div>`)
        },
        error: function () {
            jobIdSection.empty()
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
        url: `${localhost}/csv`,
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


function chooseTab1() {
    let jobCreate = $('.nav-1');
    let jobEdit = $('.nav-2');
    let csvCreate = $('.nav-3');
    let jobCreateContent = $('#content-1');
    let jobEditContent = $('#content-2');
    let csvCreateContent = $('#content-3')
    if (!(jobCreate.hasClass('active'))) {jobCreate.addClass('active')};
    jobEdit.removeClass('active');
    csvCreate.removeClass('active');
    jobCreateContent.css("display", "block");
    jobEditContent.css("display", "none");
    csvCreateContent.css("display", "none");
}


function chooseTab2() {
    let jobCreate = $('.nav-1');
    let jobEdit = $('.nav-2');
    let csvCreate = $('.nav-3');
    let jobCreateContent = $('#content-1');
    let jobEditContent = $('#content-2');
    let csvCreateContent = $('#content-3')
    if (!(jobEdit.hasClass('active'))) {jobEdit.addClass('active')};
    jobCreate.removeClass('active');
    csvCreate.removeClass('active');
    jobCreateContent.css("display", "none");
    jobEditContent.css("display", "block");
    csvCreateContent.css("display", "none");
}


function chooseTab3() {
    let jobCreate = $('.nav-1');
    let jobEdit = $('.nav-2');
    let csvCreate = $('.nav-3');
    let jobCreateContent = $('#content-1');
    let jobEditContent = $('#content-2');
    let csvCreateContent = $('#content-3')
    if (!(csvCreate.hasClass('active'))) {csvCreate.addClass('active')};
    jobCreate.removeClass('active');
    jobEdit.removeClass('active');
    jobCreateContent.css("display", "none");
    jobEditContent.css("display", "none");
    csvCreateContent.css("display", "block");
}
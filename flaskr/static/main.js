const localhost = "http://127.0.0.1:5000";

function splitUrlen(url) {
    let arr = url.split('jobs/');
    return arr.length;
}


$(document).ready(function () {
    let url = document.location.href;
    console.log(url);
    let num = "";
    if (splitUrlen(url) === 2) {
        num = url.split(url)[1]
    }
    let url1 = `${localhost}/`
    let url2 = `${localhost}/jobs`
    let url3 = `${localhost}/jobs/${num}`
    let url4 = `${localhost}/api/task-running`;

    console.log(`url1: ${url1}`);
    console.log(`url2: ${url2}`);
    console.log(`url3:` ${url3});
    if (url === url1) {
        let jobList = $('.job-list');
        jobList.empty();
        $.ajax({
            type: "GET",
            url: `${localhost}/jobs`,
            success: function (response) {
                console.log(response);
                jobs = response;
                for (let i = 0; i < jobs.length; i++) {
                    if (jobs[i] !== null) {
                        job = JSON.stringify(jobs[i])
                        let tempHtml = `<div>${job}</div><br><br>`
                        jobList.append(tempHtml)
                    }
                }
            }
        })
    }
    else if (url === url2) {
        let jobList = $('.job-list');
        jobList.empty();
        $.ajax({
            type: "GET",
            url: `${localhost}/jobs`,
            success: function (response) {
                console.log(response);
                jobs = response;
                for (let i = 0; i < jobs.length; i++) {
                    if (jobs[i] !== null) {
                        job = JSON.stringify(jobs[i])
                        let tempHtml = `<div>${job}</div><br><br>`
                        jobList.append(tempHtml)
                    }
                }
            }
        })
    } else if (url === url3) {
        let jobList = $('.job-list');
        jobList.empty();
        $.ajax({
            type: "GET",
            url: `${localhost}/api/task-running`,
            success: function (response) {
                console.log('url3')
                console.log(response);
            }
        })
    }
    else if (url === url4) {
        return;
    }
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


function addFileName() {
    let fileBox = $('.file-box');
    fileBox.on('change', )
}
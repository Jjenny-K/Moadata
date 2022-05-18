const localhost = "http://127.0.0.1:5000";


function splitUrlen(url) {
    let arr = url.split('jobs/');
    return arr.length;
}


function guideUrl() {
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
    console.log(`url3: ${url3}`);
    if (url === url1) {
        let jobList = $('.job-list');
        jobList.empty();
        $.ajax({
            type: "POST",
            url: `${localhost}/`,
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
    } else if (url === url2) {
        let jobList = $('.job-list');
        jobList.empty();

    } else if (url === url3) {
        let jobList = $('.job-list');
        jobList.empty();

    } else if (url === url4) {
        return;
    }
};


function postJob() {
    let jobName = $('.get-job-name').val();
    let columnName = $('.get-column-name').val();
    let filePath = $('.get-file-path').val();
    if (jobName === "" || columnName === "" || filePath === "") {
        alert('값을 모두 입력하시고 Task를 반드시 선택해주세요')
        return;
    }
    let readTask = $('.read-task').val();
    let dropTask = $('.drop-task').val();
    if (readTask === 'Select Read Task' || dropTask === 'Select Drop Task') {
        alert('Task를 반드시 선택해 주세요.')
        return;
    }
    let queryString = $("form[name=jobCreateForm]").serialize();
    $.ajax({
        type: 'post', url: '/api/jobs',
        data: queryString,
        dataType: 'json',
        error: function (xhr, status, error) {
            alert(error);
        }, success: function (json) {
            alert(json)
        }
    });
}


function patchJob() {
    console.log("patchJob execute");
    let jobId = $('.job_id').val();
    let jobName = $('.job_name').val();
    let columnName = $('.column_name').val();
    console.log(jobId, jobName, columnName);
    if (jobId === "" || jobName === "" || columnName === "") {
        alert('값을 다 입력하세요');
        return;
    }
    let editInfo = `{"job_id": ${jobId}, "name": ${jobName}, "column": ${columnName}`;
    $.ajax({
        method: "PATCH",
        url: `${localhost}/api/job?job_id=${jobId}&name=${jobName}&column=${columnName}`,
        contentType: 'application/json-patch+json; charset=utf-8',
        // data: JSON.stringify(editInfo),
        success: function (response) {
            console.log(response);
            alert('전송 성공.');
        },
        error: function (error) {
            console.log('전송실패');
            alert(error);
        }
    })
}


function getJob() {
    console.log("getJob execute");
    let jobId = $('.get-job-id').val();
    let jobIdSection = $('.get-job-section');
    console.log(jobId);
    console.log(jobIdSection);
    if (jobId === "") {
        alert('값을 입력하세요.');
        return;
    }
    $.ajax({
        type: "GET",
        url: `${localhost}/api/job?job_id=${jobId}`,
        success: function (response) {
            console.log(response);
            alert('조회 성공.');
            jobIdSection.empty()
            jobIdSection.append(`<div>${response}</div>`)
        },
        error: function (error) {
            jobIdSection.empty()
            alert(error)
            console.log("조회 실패");
        }
    })
};


function deleteJob() {
    console.log("deleteJob execute");
    let jobId = $('.del-job-id').val();
    let jobIdSection = $('.get-job-section');
    if (jobId === "") {
        alert('값을 입력하세요.');
        return;
    }
    $.ajax({
        method: "DELETE",
        url: `${localhost}/job?job_id=${jobId}`,
        success: function (response) {
            jobIdSection.empty()
            console.log(response);
            alert(`jobId${jobId}가 삭제되었습니다.`);
        },
        error: function (error) {
            jobIdSection.empty()
            alert(error)
            console.log(`jobId${jobId} 삭제가 실패하였습니다.`);
        }
    })
};


function addFileName() {
    let fileBox = $('.file-box');
    fileBox.on('change',)
}
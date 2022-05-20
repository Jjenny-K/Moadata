// 배포시 localhost의 주소를 바꾸어 주어야 함
const localhost = "http://127.0.0.1:5000";


$(document).ready(function () {
    let url = document.location.href;
    console.log(url);
    if (url === `${localhost}/`) {
        $.ajax({
            url: `${localhost}/api/jobs`
            , method: 'GET'
            , success: paintJobList
        })
    } else if (url === `${localhost}/client/edit`) {
        $.ajax({
            url: `${localhost}/api/jobs`
            , method: 'GET'
            , success: paintJobList2
        })
    } else if (url === `${localhost}/client/csv`) {
        $.ajax({
            url: `${localhost}/api/jobs`
            , method: 'GET'
            , success: paintJobList3
        })
    }
});


function objToDict(item) {
    return JSON.parse(JSON.stringify(item));
}


function paintJobList(res) {
    item = objToDict(res);
    $('.table-body').empty();
    let result = "";
    for (let i = 0; i < item.length; i++) {
        let property = JSON.stringify(objToDict(item[i]['property']))
        let task_list = JSON.stringify(objToDict(item[i]['task_list']))
        result += '<tr>'
        result += `<td>${item[i]['job_id']}</td>`
        result += `<td class="table-active">${item[i]['job_name']}</td>`
        result += `<td>${property}</td>`
        result += `<td class="table-active">${task_list}</td>`
        result += '</tr>'
        if (i === 50) break;
    }
    $('.table-body').append(result);
}


function paintJobList2(res) {
    item = objToDict(res);
    $('.table-body2').empty()
    let result = "";
    for (let i = 0; i < item.length; i++) {
        let property = JSON.stringify(objToDict(item[i]['property']))
        let task_list = JSON.stringify(objToDict(item[i]['task_list']))
        result += '<tr>'
        result += `<td>${item[i]['job_id']}</td>`
        result += `<td class="table-active">${item[i]['job_name']}</td>`
        result += `<td>${property}</td>`
        result += `<td class="table-active">${task_list}</td>`
        result += '</tr>'
    }
    $('.table-body2').append(result);
}


function paintJobList3(res) {
    item = objToDict(res);
    $(`.table-body-3`).empty();
    let result = "";
    for (let i = 0; i < item.length; i++) {
        let property = JSON.stringify(objToDict(item[i]['property']))
        let task_list = JSON.stringify(objToDict(item[i]['task_list']))
        result += '<tr>'
        result += `<td>${item[i]['job_id']}</td>`
        result += `<td class="table-active">${item[i]['job_name']}</td>`
        result += `<td>${property}</td>`
        result += `<td class="table-active">${task_list}</td>`
        result += '</tr>'
    }
    $(`.table-body-3`).append(result);
}


function paintGetJob(res) {
    item = objToDict(res);
    $('.table-body2').empty();
    console.log(item);
    let result = "";
    let jobId = objToDict(item)['job_id'];
    let jobName = objToDict(item)['job_name'];
    let property = JSON.stringify(objToDict(item['property']))
    let task_list = JSON.stringify(objToDict(item['task_list']))
    result += '<tr>'
    result += `<td>${jobId}</td>`
    result += `<td class="table-active">${jobName}</td>`
    result += `<td>${property}</td>`
    result += `<td class="table-active">${task_list}</td>`
    result += '</tr>'

    $('.table-body2').append(result);
}


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
    console.log(queryString);
    $.ajax({
        method: 'POST', url: '/api/jobs',
        data: queryString,
        dataType: 'json',
        contentType: "application/x-www-form-urlencoded",
        error: function (xhr, status, error) {
            alert(error);
        }, success: function (res) {
            console.log(res);
            alert('job 생성');
            window.location.reload();
        }
    });
}


function patchJob() {
    console.log("patchJob execute");
    let jobId = $('.job_id').val();
    let jobName = $('.name').val();
    let columnName = $('.name').val();
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
            $.ajax({
                url: `${localhost}/api/jobs`
                , method: 'GET'
                , success: paintJobList2
            })
            alert('전송 성공.');
            window.location.reload();
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
    console.log(jobId);
    if (jobId === "") {
        alert('값을 입력하세요.');
        return;
    }
    $.ajax({
        method: "GET",
        url: `${localhost}/api/job?job_id=${jobId}`,
        success: function (response) {
            paintGetJob(response);
            alert(`jobId: ${jobId} 조회 성공`);
        },
        error: function (error) {
            alert('해당 아이디가 없습니다')
            console.log(`jobId${jobId}조회 실패`);
        }
    })
};


function deleteJob() {
    console.log("deleteJob execute");
    let header = "X-CSRF-TOKEN";
    let jobId = $('.del-job-id').val();
    if (jobId === "") {
        alert('값을 입력하세요.');
        return;
    }
    $.ajax({
        method: "DELETE",
        url: `${localhost}/api/job?job_id=${jobId}`,
        contentType: "application/json; charset=utf-8",
        dataType: "text",
        success: function (response) {
            console.log(response);
            alert(`jobId: ${jobId}가 삭제되었습니다.`);
            window.location.reload();
        },
        error: function (error) {
            alert(error)
            console.log(`jobId: ${jobId} 삭제가 실패하였습니다.`);
        }
    })
};


function csvSuccessOrFail() {
    let filename = $('.custom-file-input')[0];
    console.log(`file: ${filename}`);
    let jobId = $('.csv-job-id').val();
    if (filename.files.length === 0 || jobId === "") {
        alert('파일 하나와 id를 모두 입력하세요.');
        return;
    }
    const formData = new FormData();
    formData.append("filename", filename.files[0]);
    formData.append('job_id', jobId);
    $.ajax({
        processData: false,
        contentType: false,
        cache: false,
        method: "POST",
        url: `${localhost}/api/task-running`,
        data: formData,
        success: function (rtn) {
            const message = rtn.data.values[0];
            console.log("message: ", message);
            alert(`서버${meesage.uploadFilePath}에 csv 파일이 수정되었습니다.`);
        },
        error: function (err) {
            console.log("err:", err);
            alert('실패하였습니다');
        },
    })
}
$(document).ready(function () {
    let jobList = document.querySelector('.job-list');
    jobList.innerHTML = "";
    $.ajax({
        type: "GET",
        url: "https://dummyjson.com/products",
        success: function (response) {
            jobs = response.products;
            indent = '&nbsp;&nbsp;&nbsp;&nbsp;'
            for (let i = 0; jobs.length <= 30; i++) {
                console.log(jobs[i]);
                let tempHtml = `<div>{<br>
                            <span style='color:red'>${indent}id:</span> <span style="color:darkblue">${jobs[i].id}</span><br>
                            ${indent}<span style='color:red'>title:</span> <span style="color:darkblue">${jobs[i].title}</span><br>                          
                            }<br>
                            </div>`

                jobList.innerHTML += tempHtml
                if (i === 50) break;
            }
        }

    })
});


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
        url: "http://127.0.0.1:5000/jobs",
        data: {data: queryString},
        success: function (response) {
            console.log(response);
            alert('삭제되었습니다.');
        }
    })
};

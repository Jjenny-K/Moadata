const uploadFile = document.getElementById('customFile');

const fileEvent = (e) => {
    const reader = new FileReader();
    console.dir(e);
    reader.readAsText(e.target.files[0]);
    window.setTimeout(() => {
        reader.onload = () => {
            console.log('파일 업로드 완료.');
        };
    }, 2000);
}

uploadFile.addEventListener('change', fileEvent);

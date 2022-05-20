from config import basedir


def test_create_tasks(api, test_create_job):
    job_id = test_create_job['job_id']
    url = "http://127.0.0.1:5000/api/task-running"

    payload = {'job_id': job_id}
    files = [
        ('filename', (
            'test.csv', open(f'{basedir}/test.csv', 'rb'),
            'text/csv'))
    ]

    response = api.post(url, data=payload, files=files)
    assert response.status_code == 201

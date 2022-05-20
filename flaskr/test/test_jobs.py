import pytest

from flaskr import app


@pytest.fixture
def api():
    api = app.test_client()

    return api


@pytest.fixture
def test_create_job(api):
    payload = {'job': 'test',
               'column': 'test',
               'file': 'test.csv',
               'read': 'None',
               'drop': 'None'}
    url = 'http://52.78.203.26:5000/api/jobs'
    response = api.post(url, payload)
    assert response.status_code == 201
    return response.text


def test_read_jobs(api):
    url = 'http://127.0.0.1:5000/api/jobs'
    response = api.get(url)
    assert response.status_code == 200


def test_read_job(api, test_create_job):
    job_id = test_create_job['job_id']
    url = f'http://127.0.0.1:5000/api/jobs?job_id={job_id}'
    response = api.get(url)
    assert response.status_code == 200


def test_delete_job(api, test_create_job):
    job_id = test_create_job['job_id']
    url = f'http://127.0.0.1:5000/api/jobs?job_id={job_id}'
    response = api.delete(url)
    assert response.status_code == 204

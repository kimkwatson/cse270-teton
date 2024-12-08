import pytest
import requests

def test_unauthorized_user(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'admin'}
    
    # Mocking the response of requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.headers = {'Content-Type': 'text/plain'}
    mock_response.text = ""
    
    mocker.patch('requests.get', return_value=mock_response)
    
    response = requests.get(url, params=params)
    
    # Assert that the response status code is 401
    assert response.status_code == 401
    
    # Assert that the Content-Type is text (not JSON)
    assert 'text' in response.headers['Content-Type']
    
    # Assert that the response body is empty
    assert response.text == ""

def test_authorized_user(mocker):
    url = "http://127.0.0.1:8000/users"
    params = {'username': 'admin', 'password': 'qwerty'}
    
    # Mocking the response of requests.get
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.headers = {'Content-Type': 'text/plain'}
    mock_response.text = ""
    
    mocker.patch('requests.get', return_value=mock_response)
    
    response = requests.get(url, params=params)
    
    # Assert that the response status code is 200
    assert response.status_code == 200
    
    # Assert that the Content-Type is text (not JSON)
    assert 'text' in response.headers['Content-Type']
    
    # Assert that the response body is empty
    assert response.text == ""

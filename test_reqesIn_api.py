import py
import pytest
import requests
from .requestApi import get_api1

@pytest.mark.get
def test_list_user():
    s = requests.session()
    result = get_api1()
    assert result.status_code == 200 


if __name__ == '__main__':
    pytest.main()
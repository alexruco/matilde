# tests/test_utils.py

import pytest
from bertha.utils import check_http_status

def test_check_http_status():
    url = "https://example.com"
    status_code = check_http_status(url)

    assert isinstance(status_code, int)
    assert status_code == 200  # Assuming the site is up

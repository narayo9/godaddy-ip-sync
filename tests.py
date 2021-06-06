import os
from pprint import pprint

import pytest
import requests

from urls import GoDaddyUrls, IFCONFIG_HOST
from utils import get_authorization_headers

TEST_DOMAIN = os.environ["TEST_DOMAIN"]
TEST_API_KEY = os.environ["TEST_API_KEY"]
TEST_API_SECRET = os.environ["TEST_API_SECRET"]
authorization_headers = get_authorization_headers(TEST_API_KEY, TEST_API_SECRET)


def test_get_my_records():
    res = requests.get(
        GoDaddyUrls.GET_DOMAIN.format(domain=TEST_DOMAIN),
        headers=authorization_headers,
    )
    res.raise_for_status()
    # pprint(res.json())


def test_get_my_dns_records():
    res = requests.get(
        GoDaddyUrls.GET_DOMAIN_DNS_RECORD.format(
            domain=TEST_DOMAIN, type="A", name="@"
        ),
        headers=authorization_headers,
    )
    res.raise_for_status()
    # pprint(res.json())


def test_get_my_ip():
    res = requests.get(IFCONFIG_HOST)
    res.raise_for_status()
    # pprint(res.text)
